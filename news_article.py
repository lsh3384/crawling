from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pymysql
import pandas as pd

crawling_db = pymysql.connect(
    user='root',
    passwd='00000000',
    host='127.0.0.1',
    db='crawling',
    charset='utf8'
)

cursor = crawling_db.cursor(pymysql.cursors.DictCursor)

# Setup opitons
option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
option.add_argument('disable-gpu')

# Selenium 4.0 - load webdriver
try:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=option)
except Exception as e:
    print(e)

# Move to URL
print("browser")
driver.get("https://star.mbn.co.kr/view.php?year=2022&no=673213&refer=portal")
driver.maximize_window()


# article title
elem = driver.find_element(By.XPATH, '//*[@id="article"]/h2')
article_title = elem.text
print('제목: ', end=' ')
print(article_title.split('\n')[0])


# article content
elem = driver.find_element(By.XPATH, '//*[@id="newsViewArea"]')
split_elem = elem.text.split('\n')
l = list(filter(None, split_elem))
article_txt = ' '.join(l)
print('내용: ', end=' ')
print(article_txt)


sql = "select count(*) from article where url = %s;"
cursor.execute(sql, driver.current_url)
article_count = cursor.fetchone()
article_count = int(article_count['count(*)'])


if article_count < 1:
    sql = 'insert into article(url, keyword, title, content) values(%s, %s, %s, %s);'
    data = (driver.current_url, '윌스미스 사과', article_title, article_txt)
    cursor.execute(sql, data)
    crawling_db.commit()


time.sleep(20)
driver.quit()