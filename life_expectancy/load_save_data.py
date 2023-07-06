"""All code related with folders and data movimentation"""

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / 'data'

class LoadStrategy:
    """Strategy to Load files"""
    def load_data(self, path):
        pass

class LoadJsonStrategy(LoadStrategy):
    """Context Strategy Class to Load Json files"""
    def load_data(self, path):
        return pd.read_json(path, compression="infer")

class LoadCsvStrategy(LoadStrategy):
    """Strategy Class to Load csv files"""
    def load_data(self, path):
        data = pd.read_csv(path, sep='\t')
        descrip_column = data.columns[0]
        data = data.melt(id_vars = descrip_column)
        data[['unit','sex', 'age', 'region']] = data[descrip_column].str.split(',', expand=True)

        data['value'] = (data['value'].
                         str.extractall(r'(\d+.\d+)').
                         astype(float)
                         .unstack().max(axis=1))
        data['value'] = pd.to_numeric(data['value'], errors='coerce')
        data['year'] = data['variable'].astype(int)

        data = data.dropna(axis = 0)
        return data

def save_data(df: pd.DataFrame, region: str) -> None:
    """Save data to a CSV file"""
    name_file = DATA_DIR / f"{region.lower()}_life_expectancy.csv"
    filepath = Path(name_file)
    df.to_csv(filepath, index=False)
