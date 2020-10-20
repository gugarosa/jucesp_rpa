# Defines the files' names
HTML_FILE="output.html"
CSV_FILE="output.csv"

# Performs the advanced search and saves a .html
python advanced_search.py $HTML_FILE

# Cleans the .html into a .csv
python parse_html.py $HTML_FILE $CSV_FILE

# Uses the .csv to dump company information
python get_information.py $CSV_FILE
