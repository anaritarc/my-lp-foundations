"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data
from . import FIXTURES_DIR

def test_clean_data():
    """Clean data testing"""
    expected_data = pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
    raw_data = pd.read_csb(FIXTURES_DIR / "eu_life_expectancy_expected")
    actual = clean_data(raw_data, "pt")
    pd.assert_frame_equal(actual, expected_data)
