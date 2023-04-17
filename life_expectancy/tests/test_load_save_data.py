"""Tests for the cleaning module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.load_save_data import load_data, save_data
from . import FIXTURES_DIR


def test_load_data():
    raw_data = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.tsv")
    pd.assertIsInstance(raw_data, pd.DataFrame)

def test_save_data():
    data = load_data(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
    expected_data = FIXTURES_DIR / "pt_life_expectancy.csv"   
    with patch.object(data, "to_csv") as to_csv_mock:
        save_data(data, region = "Pt")
        pd.assertTrue(pd.csv_file.exists())
