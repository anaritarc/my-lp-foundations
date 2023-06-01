"""Clean data code all actions needed to clean the code"""

import pandas as pd


def clean_data(data: pd.DataFrame, region: str) -> pd.DataFrame:
    """"Function to clean the data"""
    if len(data.column) < 8:
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

    data = data[['unit', 'sex', 'age', 'region', 'year', 'value']]

    data_by_region = data[data.region.str.lower() == region.lower()]
    return data_by_region
