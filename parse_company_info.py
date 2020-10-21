import argparse
import csv
import glob

from bs4 import BeautifulSoup


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Parses companies .html into a readable .csv.')

    parser.add_argument('output_file', help='Output .csv file', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathering variables from arguments
    output_file = args.output_file

    print(f'Finding files from: companies/')

    # Gets every possible file
    files = glob.glob('companies/*.html')

    print('Files found.')

    print('Extracting data ...')

    # Creates an empty list
    rows = []

    # Iterates through every file
    for f in files:
        # Parses with BeautifulSoup
        soup = BeautifulSoup(open(f).read(), features='html.parser')
        
        # Finds all <span> tags that reflects the desired information
        info = soup.find_all('span')

        # Extracting text from the found tags
        row = [i.text for i in info]

        # Appends to the output list
        rows.append(row)

    print('Data extracted.')

    print(f'Outputting data to: {output_file}')

    # Opens an output CSV file
    with open(output_file, 'w') as f:
        # Creates the writer
        writer = csv.writer(f, delimiter=';')

        # Outputs to file
        writer.writerows(rows)

    print('Data outputted.')
