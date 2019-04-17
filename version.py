import pymysql
"""
第1个参数指定连接的数据库的ip，
第2个参数指定用户名，
第3个参数指定密码，
第4个参数可有可无指定数据库名
"""
try:
    db = pymysql.connect('localhost', 'root', '', 'shop')
    # 游标也就是数据库中的指针，用来移动数据库位置，类似于文件指针
    cursor = db.cursor()
    # 执行指定的SQL语句用来获取数据库版本
    cursor.execute('SELECT VERSION()')
    # fetcgone只取一条记录，从最上面取
    data = cursor.fetchone()
    db.close()
except:
    print("关闭数据库")
print(data)