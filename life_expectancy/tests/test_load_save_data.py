"""Tests for the load and save module"""
from unittest.mock import patch
import pytest
import pandas as pd
from life_expectancy.load_save_data import LoadJsonStrategy, LoadCsvStrategy, save_data
from . import OUTPUT_DIR

@pytest.mark.parametrize("strategy_class", [LoadCsvStrategy, LoadJsonStrategy])
def test_load_data(strategy_class, raw_data):
    with patch("life_expectancy.load_save_data.pd.read_csv") as mock_read_csv, \
         patch("life_expectancy.load_save_data.pd.read_json") as mock_read_json:

        if strategy_class == LoadCsvStrategy:
            mock_read_csv.return_value = raw_data
            strategy = LoadCsvStrategy()
        elif strategy_class == LoadJsonStrategy:
            mock_read_json.return_value = raw_data
            strategy = LoadJsonStrategy()

        result = strategy.load_data()
        assert isinstance(result, pd.DataFrame)
        assert result.notnull().all().values

def test_save_data(pt_life_expectancy_expected) -> None:
    with patch.object(pt_life_expectancy_expected, "to_csv") as to_csv_mock:
        save_data(pt_life_expectancy_expected,'pt')
        to_csv_mock.assert_called_with(OUTPUT_DIR / "pt_life_expectancy.csv", index=False)
