import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx')

city_input = '//*[@id="ctl00_cphContent_frmBuscaAvancada_txtMunicipio"]'
click = '//*[@id="ctl00_cphContent_frmBuscaAvancada_btPesquisar"]'

driver.find_element_by_xpath(city_input).send_keys('araraquara')

driver.find_element_by_xpath(click).click()

driver.implicitly_wait(3)

captcha = '/html/body/div[3]/form/div[3]/div[4]/div[2]/div/div/table/tbody/tr[1]/td/div/div[1]/img'

img = driver.find_element_by_xpath(captcha)
src = img.get_attribute('src')

# download the image
urllib.request.urlretrieve(src, "captcha.png")

# output = '//*[@id="jo_resultado"]'

# print(driver.find_element_by_xpath(output))

driver.close()

