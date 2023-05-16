"""Tests for the load and save module"""
from unittest.mock import patch
import unittest.mock as mock # pylint: disable=consider-using-from-import
import pandas as pd
from life_expectancy.load_save_data import load_data, save_data
from . import OUTPUT_DIR


def test_load_data() -> None:
    """test load_data is a panda dataframe"""
    raw_data = load_data()
    assert isinstance(raw_data, pd.DataFrame)

@patch("life_expectancy.load_save_data.pd.read_table")
def test_save_data(pt_life_expectancy_expected) -> None:
    with mock.patch.object(pt_life_expectancy_expected, "to_csv") as to_csv_mock:
        save_data(pt_life_expectancy_expected,'pt')
        to_csv_mock.assert_called_with(OUTPUT_DIR / "pt_life_expectancy.csv", index=False)
