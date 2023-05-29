"""Pytest configuration file"""
import zipfile
import pandas as pd
import pytest
from . import FIXTURES_DIR, OUTPUT_DIR

@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)

@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv")

@pytest.fixture(scope="session")
def eurostat_life_expect() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    zip_file_path = FIXTURES_DIR / "eurostat_life_expect.zip"
    with zipfile.ZipFile(zip_file_path) as zip_ref:
        json_filename = zip_ref.namelist()[0]
        zip_ref.extract(json_filename)
        with zip_ref.open(json_filename) as json_file:
            json_data = json_file.read().decode('utf-8')
            return pd.read_json(json_data)

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def fr_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR/"fr_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR/"eu_life_expectancy_raw.tsv", sep='\t')
