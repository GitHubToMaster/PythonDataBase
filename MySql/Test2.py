import pymysql
db = pymysql.connect('127.0.0.1', 'root', '', 'shop')
cursor = db.cursor()

# 查询语句返回的是一个元祖
cursor.execute("SELECT * from telphone")
data = cursor.fetchall()
print(type(data))
for phone in data:
    print("手机型号：", phone[1])
