import argparse
import csv
import time
import urllib.request

from selenium import webdriver

import paths.advanced_search as s
import paths.company_info as i
import utils.captcha as c


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Loads a companies .csv and extracts information over JUCESP.')

    parser.add_argument('input_file', help='Input .csv file', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathering variables from arguments
    input_file = args.input_file
    captcha_file = 'captcha.png'

    # Creates the webdriver
    driver = webdriver.Firefox()
    driver.implicitly_wait(s.WAITING_TIME)

    # Gets the search URL and uses a caveat to only input captcha once
    driver.get(s.URL)
    driver.find_element_by_xpath(s.FORM_SUBMIT).click()
    img = driver.find_element_by_xpath(s.CAPTCHA)
    urllib.request.urlretrieve(img.get_attribute('src'), captcha_file)
    solved_captcha = c.solve(captcha_file)
    driver.find_element_by_xpath(s.CAPTCHA_INPUT).send_keys(solved_captcha)
    driver.find_element_by_xpath(s.CAPTCHA_SUBMIT).click()

    # Loads the input .csv file
    with open(input_file) as f:
        # Creates an .csv reader
        reader = csv.reader(f, delimiter=',')

        # Iterates over the reader
        for row in reader:
            print(f'Dumping data from ID: {row[0]} ...')

            # Gets the URL
            driver.get(i.URL + row[0])

            # Sleeps for a short amount of time
            time.sleep(i.WAITING_TIME)

            # Gathers the results
            results = driver.find_element_by_xpath(i.RESULTS).get_attribute('outerHTML')

            # Opens an output file
            with open(f'companies/{row[0]}.html', 'w') as f2:
                f2.write(results)

            print('Data dumped.')

    driver.close()
