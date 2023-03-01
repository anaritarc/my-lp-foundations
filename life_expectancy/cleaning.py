"""Python version 3.11.2 """

from pathlib import Path
import pandas as pd

def load_data():
    """Get data from a tsv"""
    p_raw_d = Path('./life_expectancy/data/eu_life_expectancy_raw.tsv')
    return pd.read_csv(p_raw_d, sep='\t')

def save_data(df): # pylint: disable=invalid-name
    """Save data in a csv"""
    filepath = Path('./life_expectancy/data/pt_life_expectancy.csv')
    df.to_csv(filepath, index = False)

def clean_data(raw_data, reg):  # pylint: disable=missing-function-docstring
    descrip_column = raw_data.columns[0]
    data = raw_data.melt(id_vars = descrip_column)
    data[['unit','sex', 'age', 'region']] = data[descrip_column].str.split(',', expand=True)

    data['value'] = data['value'].str.extractall(r'(\d+.\d+)').astype(float).unstack().max(axis=1)
    data['value'] = pd.to_numeric(data['value'], errors='coerce')
    data['year'] = data['variable'].astype(int)

    data = data.dropna(axis = 0)
    data = data[['unit', 'sex', 'age', 'region', 'year', 'value']]

    data_by_region = data[data.region.str.lower() == reg.lower()]
    return data_by_region

def main(reg='pt'):  # pylint: disable=missing-function-docstring
    raw_data = load_data()
    data_by_region = clean_data(raw_data, reg)
    save_data(data_by_region)
    