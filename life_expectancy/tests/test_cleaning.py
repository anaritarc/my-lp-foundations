"""Tests for the cleaning module"""
import unittest
import pandas as pd
from life_expectancy.load_save_data import load_data, save_data
from life_expectancy.cleaning import clean_data
from life_expectancy.pipeline import main
from . import OUTPUT_DIR, FIXTURES_DIR

class TestCleanData(unittest.TestCase):
    """Clean data testing, for all functions"""

    def setUp(self):
        self.raw_data = load_data()
        self.cleaned_data = clean_data(self.raw_data, 'pt')
        self.csv_file = OUTPUT_DIR / "pt_life_expectancy.csv"
        self.csv_file_fr = OUTPUT_DIR / "fr_life_expectancy.csv"
        self.expected_data = pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

    def test_load_data(self):
        self.assertIsInstance(self.raw_data, pd.DataFrame)

    def test_clean_data(self):
        cols = ['unit', 'sex', 'age', 'region', 'year', 'value']
        self.assertListEqual(list(self.cleaned_data.columns), cols)
        self.assertEqual(self.cleaned_data['year'].dtype, int)
        self.assertEqual(self.cleaned_data['value'].dtype, float)

    def test_save_data(self):
        save_data(self.cleaned_data, region = "Pt")
        self.assertTrue(self.csv_file.exists())

    def test_main_default_region(self):
        try:
            main()
        except NameError:
            exit()  # pylint: disable=consider-using-sys-exit

    def test_main_different_region(self):
        main('fr')
        self.assertTrue(self.csv_file_fr.exists())

if __name__ == '__main__':
    unittest.main()
