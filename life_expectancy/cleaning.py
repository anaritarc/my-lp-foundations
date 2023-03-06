"""Clean data code"""

import argparse
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / 'data'

def load_data() -> pd.DataFrame:
    """Get data from a tsv"""
    name_file = DATA_DIR / "eu_life_expectancy_raw.tsv"
    return pd.read_csv(name_file, sep='\t')

def _save_data(df) -> None: # pylint: disable=invalid-name
    """Save data in a csv"""
    name_file = DATA_DIR / "pt_life_expectancy.csv"
    filepath = Path(name_file)
    df.to_csv(filepath, index = False)

def clean_data(raw_data: pd.DataFrame, region: str) -> pd.DataFrame:
    descrip_column = raw_data.columns[0]
    data = raw_data.melt(id_vars = descrip_column)
    data[['unit','sex', 'age', 'region']] = data[descrip_column].str.split(',', expand=True)

    data['value'] = data['value'].str.extractall(r'(\d+.\d+)').astype(float).unstack().max(axis=1)
    data['value'] = pd.to_numeric(data['value'], errors='coerce')
    data['year'] = data['variable'].astype(int)

    data = data.dropna(axis = 0)
    data = data[['unit', 'sex', 'age', 'region', 'year', 'value']]

    data_by_region = data[data.region.str.lower() == region.lower()]
    return data_by_region

def main(region: str) ->None:
    raw_data = load_data()
    data_by_region = clean_data(raw_data, region)
    print(data_by_region.head())
    _save_data(data_by_region)


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--region", help="Select data region", type=str, default ='pt')
    args = parser.parse_args()
    main(args.region)
