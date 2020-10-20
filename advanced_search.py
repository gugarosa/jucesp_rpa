import argparse
import time
import urllib.request

from selenium import webdriver

import utils.captcha as c
import utils.search_path as p


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Performs an advanced search over JUCESP.')

    parser.add_argument('output_file', help='Output .html file', type=str)

    parser.add_argument('-captcha_file', help='Identifier to the captcha file', type=str, default='captcha.png')

    return parser.parse_args()

if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathering variables from arguments
    output_file = args.output_file
    captcha_file = args.captcha_file

    print('Starting up the driver ...')

    # Creates the webdriver and gets the URL
    driver = webdriver.Firefox()
    driver.get(p.URL)
    driver.implicitly_wait(p.WAITING_TIME)

    print('Driver initialized.')

    print('Filling out the form ...')

    # Iterates through the form
    for k, v in p.FORM.items():
        # Fills out the form
        driver.find_element_by_xpath(v[0]).send_keys(v[1])

    # Submits the form and awaits for response
    driver.find_element_by_xpath(p.FORM_SUBMIT).click()

    print('Form submitted.')

    print('Retrieving and solving captcha ...')

    # Retrieves and downloads the captcha
    img = driver.find_element_by_xpath(p.CAPTCHA)
    urllib.request.urlretrieve(img.get_attribute('src'), captcha_file)

    # Solves the captcha, inputs it, submits the form and awaits for response
    solved_captcha = c.solve(captcha_file)
    driver.find_element_by_xpath(p.CAPTCHA_INPUT).send_keys(solved_captcha)
    driver.find_element_by_xpath(p.CAPTCHA_SUBMIT).click()

    print('Captcha solved.')

    print('Dumping data ...')

    # Opens an output file
    with open(output_file, 'w') as f:
        # Starts the loop
        while True:
            # Sleeps for a short amount of time
            time.sleep(p.WAITING_TIME)

            # Gathers the results table
            results = driver.find_element_by_xpath(p.RESULTS).get_attribute('outerHTML')

            # Writes the results
            f.write(results)

            # Tries to find the next page href
            try:
                # Finds the element
                next_page = driver.find_element_by_xpath(p.RESULTS_NEXT_PAGE)

            # If element could not be found
            except:
                # Breaks the loop
                break

            # Executes the script
            driver.execute_script(p.RESULTS_NEXT_PAGE_SCRIPT)

    print('Data dumped.')

    # Closes the driver
    driver.close()
