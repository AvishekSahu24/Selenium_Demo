import os

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



chromedriver = "/usr/bin/chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

driver.get("https://www.sonyliv.com/")
# delay = 120 # seconds

# try:
#     myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
#     print("Page is ready!")
#     video = driver.find_element_by_xpath('//*[@id="movie_7"]/ul/data-owl-carousel/div/div/div[1]/li/div/custom-rails-landscape/div/a/div/div[1]/span')
#
#     video.click()
# except TimeoutException:
#     print("Loading took too much time!")
cancel = driver.find_element_by_xpath('//*[@id="wzrk-cancel"]')
cancel.click()

# video = driver.find_element_by_xpath('//*[@id="movie_5"]/ul/data-owl-carousel/div/div/div[1]/li/div/custom-rails-landscape/div/a/div/img')
#video = driver.find_element_by_xpath('//*[@id="movie_8"]/ul/data-owl-carousel/div/div/div[1]/li/div/custom-rails-landscape/div/a/div/img')
video = driver.find_element_by_xpath('//*[@id="movie_8"]/ul/data-owl-carousel/div/div/div[1]/li/div/custom-rails-landscape/div/a/div/img')

video.click()
# time.sleep(33)
#
# try:
#    skip= driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div')
#    skip.click()
# except:
#     pass

# '//*[@id="bcPlayer"]/div[9]/div[7]/div'

# video = driver.find_element_by_xpath('//*[@id="movie_7"]/ul/data-owl-carousel/div/div/div[1]/li/div/custom-rails-landscape/div/a/div/div[1]/span')
#
# video.click()
# try:
#     skip =  driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div')
#     print(skip.text)
# except:
#     pass

# '//*[@id="bcPlayer"]/div[9]/div[7]/div'

time.sleep(35)
changeTime  = driver.find_elements_by_xpath('//*[@id="bcPlayer"]/div[10]/div[5]/div')
# changeTime[0].setAttribute('aria-valuenow', '06.00')



# driver.execute_script("arguments[1].setAttribute('aria-valuenow', '06.00')", changeTime);

driver.execute_script("changeTime.attr('aria-valuenow','6.00')", changeTime)


'''

<div tabindex="0" class="vjs-progress-holder vjs-slider vjs-slider-horizontal" role="slider" aria-valuenow="0.83" aria-valuemin="0" aria-valuemax="100" aria-label="Progress Bar" aria-valuetext="0:00:38 of 1:17:41"><div class="vjs-load-progress" style="width: 1.93263%;"><span class="vjs-control-text"><span>Loaded</span>: 0%</span><div style="left: 8.9698%; width: 91.0302%;"></div></div><div class="vjs-mouse-display" style="left: 34.0178px;"><div class="vjs-time-tooltip" style="right: -19.9922px;">0:17:43</div></div><div class="vjs-play-progress vjs-slider-bar" style="width: 0.83%;"><div class="vjs-time-tooltip" style="right: -52.1371px;">0:00:38</div><span class="vjs-control-text"><span>Progress</span>: 0%</span></div></div>


'''