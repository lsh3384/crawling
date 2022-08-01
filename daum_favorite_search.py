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
driver.get("https://www.daum.net")
driver.maximize_window()


elem_id = driver.find_element(By.CLASS_NAME, 'slide_favorsch')
elem_texts = elem_id.find_elements(By.CSS_SELECTOR, 'li')
for elem in elem_texts:
    print(elem.text)

next_btn = driver.find_element(By.XPATH, '//*[@id="wrapSearch"]/div[4]/button[2]')
next_btn.click()

elem_id = driver.find_element(By.CLASS_NAME, 'slide_favorsch')
elem_texts = elem_id.find_elements(By.CSS_SELECTOR, 'li')
for elem in elem_texts:
    print(elem.text)


#
# elem_id = driver.find_element(By.CLASS_NAME, 'list_favorsch hide')
# elem_texts = elem_id.find_elements(By.CSS_SELECTOR, 'li')
# for elem in elem_texts:
#     print(elem.text)


time.sleep(200)
# driver.back()
# driver.forward()
# driver.refresh()
# print(driver.title)
# print(driver.current_url)

# Do crawling
