# Defines the files' names
HTML_FILE="advanced_search.html"
CSV_FILE="companies.csv"
COMPANY_FILE="parsed_companies.csv"

# Performs the advanced search and saves a .html
python advanced_search.py $HTML_FILE

# Cleans the advanced search .html into a .csv
python parse_advanced_search.py $HTML_FILE $CSV_FILE

# Uses the .csv to dump companies information
python company_info.py $CSV_FILE

# Parses companies information into a readable .csv
python parse_company_info.py $COMPANY_FILE
