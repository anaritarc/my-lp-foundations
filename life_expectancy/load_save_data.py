"""All code related with folders and data movimentation"""

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / 'data'

def load_data() -> pd.DataFrame:
    """Get data from a tsv"""
    name_file = DATA_DIR / "eu_life_expectancy_raw.tsv"
    return pd.read_csv(name_file, sep='\t')

def save_data(df,region) -> None: # pylint: disable=invalid-name
    """Save data in a csv"""
    name_file = DATA_DIR / f"{region.lower()}_life_expectancy.csv"
    filepath = Path(name_file)
    df.to_csv(filepath, index = False)
    