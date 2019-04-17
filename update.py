import pymysql
try:
    db = pymysql.connect('localhost', 'root', '', 'shop')
    cursor = db.cursor()
    sqlstr = r"UPDATE student SET name = 'yirufeng' where id = 123"
    cursor.execute(sqlstr)
    result = cursor.fetchall()
    print(result)
    db.commit()
    result2 = cursor.fetchall()
    print(result2)
    db.close()
except:
    print("密码错误")