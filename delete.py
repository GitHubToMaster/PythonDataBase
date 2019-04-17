import pymysql
try:
    db = pymysql.connect('localhost', 'root', '', 'shop')
    cursor = db.cursor()
    cursor.execute(r"delete from student where name='吴晓文'")
    result = cursor.fetchall()
    print(result)
    db.commit()
    print(result)
except:
    print("密码错误")
