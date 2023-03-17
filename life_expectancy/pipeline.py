"""Main with the connection of all needed modules"""

import argparse
from life_expectancy.load_save_data import load_data, save_data
from life_expectancy.cleaning import clean_data

def main(region = 'pt') ->None:
    raw_data = load_data()
    data_by_region = clean_data(raw_data, region)
    save_data(data_by_region, region)


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--region", help="Select data region", type=str, default ='pt')
    args = parser.parse_args()
    main(args.region)
