"""All code related with folders and data movimentation"""

from pathlib import Path
import json
import zipfile
import pandas as pd

DATA_DIR = Path(__file__).parent / 'data'

class LoadStrategy:
    """Strategy to Load files"""
    def load_data(self):
        pass

class LoadJsonStrategy(LoadStrategy):
    """Context Strategy Class to Load Json files"""
    def load_data(self):
        name_file = DATA_DIR / "eurostat_life_expect.zip"
        with zipfile.ZipFile(name_file, 'r') as zip_ref:
            json_filename = zip_ref.namelist()[0]
            zip_ref.extract(json_filename)
            with open(json_filename, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        return pd.DataFrame(data)

class LoadCsvStrategy(LoadStrategy):
    """Strategy Class to Load csv files"""
    def load_data(self):
        name_file = DATA_DIR / "eu_life_expectancy_raw.tsv"
        return pd.read_csv(name_file, sep='\t')

def save_data(df, region) -> None:
    """Save data to a CSV file"""
    name_file = DATA_DIR / f"{region.lower()}_life_expectancy.csv"
    filepath = Path(name_file)
    df.to_csv(filepath, index=False)
