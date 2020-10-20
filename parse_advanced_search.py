import argparse
import csv

from bs4 import BeautifulSoup


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Parses advanced search .html into a readable .csv.')

    parser.add_argument('input_file', help='Input .html file', type=str)

    parser.add_argument('output_file', help='Output .csv file', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathering variables from arguments
    input_file = args.input_file
    output_file = args.output_file

    print(f'Loading and parsing file from: {input_file}')

    # Parses with BeautifulSoup
    soup = BeautifulSoup(open(input_file).read(), features='html.parser')

    print('File loaded and parsed.')

    # Creates an empty list
    rows = []

    print('Extracting data ...')

    # Finds all tables
    tables = soup.find_all('table')

    # Iterates through all tables
    for table in tables:
        # Iterates through all rows
        for row in table.find_all('tr'):
            # Defines variables as None
            _id, name = None, None

            # Gathers the identifier column
            id_column = row.find('td', class_='item01')

            # If identifier column exists
            if id_column:
                # Gathers its ID
                _id = id_column.find('a').text

            # Gathers the name column
            name_column = row.find('td', class_='item02')

            # If name column exists
            if name_column:
                # Gathers its name
                name = name_column.find('span').text

            # Gathers the city column
            city_column = row.find('td', class_='item03')

            # If identifier column exists
            if city_column:
                # Gathers its city
                city = city_column.text

            # Checks if both variables exist
            if _id and name and city:
                # Appends to the output list
                rows.append([_id, name, city])

    print('Data extracted.')

    print(f'Outputting data to: {output_file}')

    # Opens an output CSV file
    with open(output_file, 'w') as f:
        # Creates the writer
        writer = csv.writer(f)

        # Outputs to file
        writer.writerows(rows)

    print('Data outputted.')
