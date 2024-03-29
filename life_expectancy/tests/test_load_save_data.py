"""Tests for the load and save module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.load_save_data import load_data, save_data
from . import OUTPUT_DIR


@patch("life_expectancy.load_save_data.pd.read_table")
def test_load_data(mock_read_csv, eu_life_expectancy_raw) -> None:
    """test load_data is a panda dataframe"""
    mock_read_csv.return_value = eu_life_expectancy_raw
    result = load_data()
    assert isinstance(result, pd.DataFrame)

def test_save_data(pt_life_expectancy_expected) -> None:
    with patch.object(pt_life_expectancy_expected, "to_csv") as to_csv_mock:
        save_data(pt_life_expectancy_expected,'pt')
        to_csv_mock.assert_called_with(OUTPUT_DIR / "pt_life_expectancy.csv", index=False)
