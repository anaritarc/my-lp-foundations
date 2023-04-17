"""Tests for the cleaning module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.pipeline import main
from . import FIXTURES_DIR

@patch("life_expectancy.pipeline.save_data")
def test_main_different_region():
    csv_file_fr = main(FIXTURES_DIR/"eu_life_expectancy_raw_fixture.tsv", "fr")
    pd.assertTrue(csv_file_fr.exists())


