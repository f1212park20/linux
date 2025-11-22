import pymysql

conn = pymysql.connect(
    user='flaskuser',
    password='flaskpass',
    database='testdb',
    port=3306
)

cur = conn.cursor()
cur.execute("SELECT * FROM users;")
print(cur.fetchall())

conn.close()
