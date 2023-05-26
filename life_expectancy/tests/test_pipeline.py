"""Testing pipeline code."""

import unittest
from unittest.mock import patch
from argparse import Namespace
from life_expectancy.pipeline import main

class TestMain(unittest.TestCase):
    """Pipeline testing with unittest"""
    @patch('life_expectancy.pipeline.load_data')
    @patch('life_expectancy.pipeline.clean_data')
    @patch('life_expectancy.pipeline.save_data')
    @patch('argparse.ArgumentParser.parse_args')
    def test_main(self, mock_parse_args, mock_save_data, mock_clean_data, mock_load_data):
        mock_parse_args.return_value = Namespace(region='pt')
        mock_load_data.return_value = 'raw_data'
        mock_clean_data.return_value = 'cleaned_data'
        main()
        mock_load_data.assert_called_once()
        mock_clean_data.assert_called_once_with('raw_data', 'pt')
        mock_save_data.assert_called_once_with('cleaned_data', 'pt')

if __name__ == '__main__':
    unittest.main()
