import pymysql
try:
    db = pymysql.connect('127.0.0.1', 'root', '', 'shop')
    cursor = db.cursor()
    # sqlstr = 
    cursor.execute("insert into student values('吴晓文', 123)")
    result = cursor.fetchall()
    print(result)
    # 数据库操作即刻生效
    db.commit()
    result2 = cursor.fetchall()
    print(result2)
    # 关闭数据库连接
    db.close()
except:
    print("密码错误")