import redis
try:
    myredis = redis.StrictRedis(host='127.0.0.1', port=6379,
                             db=0, password='')
    print(myredis.get('gaoqinghua'))
    myredis.set('gaoqinghua', 5)
    print(myredis.get('gaoqinghua'))
    print(type(myredis.get('gaoqinghua')))
except:
    print("密码错误")
