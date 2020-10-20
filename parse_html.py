from bs4 import BeautifulSoup
import csv

# Loads the input HTML
html = open('output.html').read()

# Parses with BeautifulSoup
soup = BeautifulSoup(html, features='html.parser')

# Creates an empty list
rows = []

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

        # Checks if both variables exist
        if _id and name:
            # Appends to the output list
            rows.append([_id, name])

# Opens an output CSV file    
with open('output.csv', 'w') as f:
    # Creates the writer
    writer = csv.writer(f)

    # Outputs to file
    writer.writerows(rows)
