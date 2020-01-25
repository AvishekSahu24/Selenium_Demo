

import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chromedriver = "/usr/bin/chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

driver.get("https://changegod.com/greenseed_yt_test47.html")


driver.find_element_by_xpath('/html/body').click()



