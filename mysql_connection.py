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

sql = "SELECT * FROM `account`;"
cursor.execute(sql)
result = cursor.fetchall()

print(result)

# sql을 실행해서 가져온 결과를 pandas의 DataFrame으로 변경해서 사용가능
result_dataframe = pd.DataFrame(result)
print(result_dataframe)


sql = '''INSERT INTO `account` (id, pw) 
    VALUES ('test_id', 'test_pw');'''
cursor.execute(sql)
crawling_db.commit() # commit을 날려야 변경사항이 db에 반영된다.