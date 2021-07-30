import redis
redisClient = redis.Redis(
    host='127.0.0.1',
    port=6379)
#redisClient.hset("NumberVsString", "1", "One")
#redisClient.hset("NumberVsString", "2", "Two")
#redisClient.hset("NumberVsString", "3", "Three")
# print("Value for the key 3 is")
#print(redisClient.hget("NumberVsString", "3"))
# print("The keys present in the Redis hash:");
# print(redisClient.hkeys("NumberVsString"))
# print("The values present in the Redis hash:");
# print(redisClient.hvals("NumberVsString"))
# print("The keys and values present in the Redis hash are:")
print(redisClient.hgetall("NumberVsString"))