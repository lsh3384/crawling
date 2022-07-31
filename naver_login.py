import selenium
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

# Setup opitons
option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
# option.add_argument("start-maximized")
option.add_argument('disable-gpu')
# option.add_argument('headless')

# Selenium 4.0 - load webdriver
try:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=option)
except Exception as e:
    print(e)

user_id = "id"
user_pw = "pw"

# Move to URL
print("browser")
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
driver.maximize_window()

elem_id = driver.find_element(By.ID, 'id')
elem_id.click()
pyperclip.copy(user_id)
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

elem_pw = driver.find_element(By.ID, 'pw')
elem_pw.click()
pyperclip.copy(user_pw)
elem_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

driver.find_element(By.ID, 'log.login').click()

driver.get("https://www.naver.com/")
time.sleep(200)
# driver.back()
# driver.forward()
# driver.refresh()
# print(driver.title)
# print(driver.current_url)

# Do crawling
