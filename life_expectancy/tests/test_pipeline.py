""""Tests for the main module"""
import unittest
from unittest.mock import patch, MagicMock
from argparse import Namespace
from life_expectancy.pipeline import main

class TestMain(unittest.TestCase):
    """Unit tests for the main function"""

    @patch('life_expectancy.pipeline.LoadJsonStrategy')
    @patch('life_expectancy.pipeline.clean_data')
    @patch('life_expectancy.pipeline.save_data')
    def test_main(self, mock_save_data, mock_clean_data, mock_load_strategy):
        mock_load_data = MagicMock()
        mock_load_data.load_data.return_value = 'raw_data'
        mock_load_strategy.return_value = mock_load_data
        mock_cleaned_data = MagicMock()
        mock_clean_data.return_value = mock_cleaned_data
        mock_save_data.return_value = None

        args = Namespace(region='pt', json_csv='json')
        main(args.region, args.json_csv)

        mock_load_strategy.assert_called_once()
        mock_load_data.load_data.assert_called_once()
        mock_clean_data.assert_called_once_with('raw_data', 'pt')
        mock_save_data.assert_called_once_with(mock_cleaned_data, 'pt')


if __name__ == '__main__':
    unittest.main()
