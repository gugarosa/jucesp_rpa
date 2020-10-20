import urllib.request
import time

from selenium import webdriver

import utils.captcha as c
import utils.paths as p

print('Creating driver ...')

# Creates the webdriver and gets the URL
driver = webdriver.Firefox()
driver.get(p.SEARCH_URL)
driver.implicitly_wait(p.WAITING_TIME)

print('Filling out form ...')

# Iterates through the form
for k, v in p.FORM.items():
    # Fills out the form
    driver.find_element_by_xpath(v[0]).send_keys(v[1])

print('Submitting form ...')

# Submits the form and awaits for response
driver.find_element_by_xpath(p.SUBMIT).click()
driver.implicitly_wait(p.WAITING_TIME)

print('Retrieving captcha ...')

# Retrieves and downloads the captcha
img = driver.find_element_by_xpath(p.CAPTCHA)
urllib.request.urlretrieve(img.get_attribute('src'), 'captcha.png')

print('Solving captcha ...')

# Solves the captcha, inputs it, submits the form and awaits for response
solved_captcha = c.solve('captcha.png')
driver.find_element_by_xpath(p.CAPTCHA_INPUT).send_keys(solved_captcha)
driver.find_element_by_xpath(p.CAPTCHA_SUBMIT).click()

print('Iterating results ...')

# Starts the loop
while True:
    # Sleeps for a short amount of time
    time.sleep(p.WAITING_TIME)

    # Gathers the results table
    results = driver.find_element_by_xpath(p.RESULTS_TABLE).get_attribute('outerHTML')

    # Appends to the output file
    with open('output.html', 'a') as f:
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

# Closes the driver
driver.close()
