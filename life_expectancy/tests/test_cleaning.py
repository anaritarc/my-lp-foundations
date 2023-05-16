"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data

def test_clean_data(pt_life_expectancy_expected, eu_life_expectancy) -> None:
    """Clean data testing"""
    actual = clean_data(eu_life_expectancy, region = 'pt').reset_index(drop=True)
    pd.testing.assert_frame_equal(actual, pt_life_expectancy_expected.reset_index(drop=True))
