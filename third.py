import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chromedriver = "/usr/bin/chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

driver.get("https://www.facebook.com/")

username= driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input')


username.send_keys('aviRandom@gmail.com')
password = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input')
password.send_keys('password')
login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login.click()
