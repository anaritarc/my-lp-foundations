"""Python version 3.11.2 """

from pathlib import Path
import pandas as pd

def get_data():
    """Get data from a tsv"""
    p_raw_d = Path('./life_expectancy/data/eu_life_expectancy_raw.tsv')
    return pd.read_csv(p_raw_d, sep='\t')

def save_data(df): # pylint: disable=invalid-name
    """Save data in a csv"""
    filepath = Path('./life_expectancy/data/pt_life_expectancy.csv')
    df.to_csv(filepath, index = False)

def convert_int_float(df):  # pylint: disable=invalid-name
    """Convert value to float and year to int"""
    df['value'] = df['value'].str.extractall(r'(\d+.\d+)').astype(float).unstack().max(axis=1)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['year'] = df['variable'].astype(int)
    return df

def drop_columns_rows(df):  # pylint: disable=invalid-name
    """Drop uneeded columns and rows"""    
    df = df.dropna(axis = 0)
    return df[['unit', 'sex', 'age', 'region', 'year', 'value']]

def to_pivot():
    """Receive data and convert it to pivot"""  
    raw_data = get_data()

    descrip_column = raw_data.columns[0]
    data = raw_data.melt(id_vars = descrip_column)
    data[['unit','sex', 'age', 'region']] = data[descrip_column].str.split(',', expand=True)
    return data

def clean_data(reg : str ='pt'):
    """Full process to clean data"""
    pivot_data = to_pivot()
    int_float_data = convert_int_float(pivot_data)
    all_cleandata = drop_columns_rows(int_float_data)

    data_by_region = all_cleandata[all_cleandata.region.str.lower() == reg.lower()]
    save_data(data_by_region)
