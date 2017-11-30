import redis


pool = redis.ConnectionPool(host='39.106.144.72',port='6379')
r = redis.Redis(connection_pool=pool)
print(r.get('foo'))


