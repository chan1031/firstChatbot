import pymysql

db= None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='root',
        db='jspdb',
        charset='utf8'
    )
    print("DB연동 성공")
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB연결 닫기 성공")