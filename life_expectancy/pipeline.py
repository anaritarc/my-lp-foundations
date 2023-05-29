"""Main with the connection of all needed modules"""

import argparse
from enum import Enum
from life_expectancy.load_save_data import LoadJsonStrategy, LoadCsvStrategy, save_data
from life_expectancy.cleaning import clean_data

class Country(Enum):
    """List of possible countries"""
    Austria = 'AT'
    Belgium = 'BE'
    Bulgaria = 'BG'
    Switzerland = 'CH'
    Cyprus = 'CY'
    Czech_Republic = 'CZ'
    Denmark = 'DK'
    Estonia = 'EE'
    Greece = 'EL'
    Spain = 'ES'
    Finland = 'FI'
    France = 'FR'
    Croatia = 'HR'
    Hungary = 'HU'
    Iceland = 'IS'
    Italy = 'IT'
    Liechtenstein = 'LI'
    Lithuania = 'LT'
    Luxembourg = 'LU'
    Latvia = 'LV'
    Malta = 'MT'
    Netherlands = 'NL'
    Norway = 'NO'
    Poland = 'PL'
    Portugal = 'PT'
    Romania = 'RO'
    Sweden = 'SE'
    Slovenia = 'SI'
    Slovakia = 'SK'
    Germany = 'DE'
    Albania = 'AL'
    Ireland = 'IE'
    Montenegro = 'ME'
    North_Macedonia = 'MK'
    Serbia = 'RS'
    Armenia = 'AM'
    Azerbaijan = 'AZ'
    Georgia = 'GE'
    Turkey = 'TR'
    Ukraine = 'UA'
    Belarus = 'BY'
    United_Kingdom = 'UK'
    Moldova = 'MD'
    Russia = 'RU'


def main(region='pt', json_csv='csv') -> None:
    strategies = {
        'json': LoadJsonStrategy(),
        'csv': LoadCsvStrategy()
    }
    data_load_strategy = strategies[json_csv.lower()]
    raw_data = data_load_strategy.load_data()
    data_by_region = clean_data(raw_data, region)
    save_data(data_by_region, region)


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r","--region", 
        help="Select data region",
        type=Country, choices=list(Country),
        default=Country.Portugal)
    parser.add_argument(
        "-f", "--json_csv", 
        help="Select output format (json/csv)",
        type=str, choices=['json', 'csv'],
        default='csv')
    args = parser.parse_args()
    main(args.region, args.json_csv)
