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

user_id = "ID"
user_pw = "PW"

# Move to URL
print("browser")
driver.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fis_popup%3Dfalse%26ka%3Dsdk%252F1.43.0%2520os%252Fjavascript%2520sdk_type%252Fjavascript%2520lang%252Fko-KR%2520device%252FWin32%2520origin%252Fhttps%25253A%25252F%25252Fwww.tistory.com%26auth_tran_id%3Duz95kaz7daab8aef3eeb03fa312b81795386484f051l69aywat%26response_type%3Dcode%26state%3DaHR0cHM6Ly93d3cudGlzdG9yeS5jb20v%26redirect_uri%3Dhttps%253A%252F%252Fwww.tistory.com%252Fauth%252Fkakao%252Fredirect%26client_id%3Db8aef3eeb03fa312b81795386484f051&talk_login=hidden")
driver.maximize_window()

elem_id = driver.find_element(By.ID, 'id_email_2')
# elem_id.click()
pyperclip.copy(user_id)
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

elem_pw = driver.find_element(By.NAME, 'password')
# elem_pw.click()
pyperclip.copy(user_pw)
elem_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(2)

driver.get("https://www.tistory.com/")
time.sleep(200)
# driver.back()
# driver.forward()
# driver.refresh()
# print(driver.title)
# print(driver.current_url)

# Do crawling
