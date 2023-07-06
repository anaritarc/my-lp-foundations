"""Clean data code all actions needed to clean the code"""

import pandas as pd


def clean_data(data: pd.DataFrame, region: str) -> pd.DataFrame:
    """"Function to clean the data"""
    data = data[['unit', 'sex', 'age', 'region', 'year', 'value']]

    data_by_region = data[data.region.str.lower() == region.lower()]
    return data_by_region
