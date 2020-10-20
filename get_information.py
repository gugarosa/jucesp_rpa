import argparse
import csv
import time
import urllib.request

from selenium import webdriver

import utils.captcha as c
import utils.info_path as p


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Loads a .csv and extract information over JUCESP.')

    parser.add_argument('input_file', help='Input .csv file', type=str)

    parser.add_argument('-captcha_file', help='Identifier to the captcha file', type=str, default='captcha.png')

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathering variables from arguments
    input_file = args.input_file
    captcha_file = args.captcha_file

    # Loads the input .csv file
    with open(input_file) as f:
        # Creates an .csv reader
        reader = csv.reader(f, delimiter=',')

        # Iterates over the reader
        for row in reader:
            print(f'Dumping data from ID: {row[0]} ...')

            # Creates the webdriver and gets the URL
            driver = webdriver.Firefox()
            driver.get(p.URL + row[0])
            driver.implicitly_wait(p.WAITING_TIME)

            # Retrieves and downloads the captcha
            img = driver.find_element_by_xpath(p.CAPTCHA)
            urllib.request.urlretrieve(img.get_attribute('src'), captcha_file)

            # Solves the captcha, inputs it, submits the form and awaits for response
            solved_captcha = c.solve(captcha_file)
            driver.find_element_by_xpath(p.CAPTCHA_INPUT).send_keys(solved_captcha)
            driver.find_element_by_xpath(p.CAPTCHA_SUBMIT).click()

            # Sleeps for a short amount of time
            time.sleep(p.WAITING_TIME)

            # Gathers the results
            results = driver.find_element_by_xpath(p.RESULTS).get_attribute('outerHTML')

            # Opens an output file
            with open(f'outputs/{row[0]}.html', 'w') as f2:
                f2.write(results)

            print('Data dumped.')

            driver.close()
