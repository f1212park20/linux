import pymysql

conn = pymysql.connect(
    host='127.0.0.1',   # MySQL 컨테이너 포트로 연결
    user='flaskuser',
    password='flaskpass',
    database='testdb',
    port=3306
)

cur = conn.cursor()
cur.execute("SELECT * FROM users;")
print(cur.fetchall())

conn.close()
