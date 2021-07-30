from flask import Flask  
import redis
redisClient = redis.Redis(
    host='127.0.0.1',
    port=6379)
app = Flask(__name__)   
 
@app.route('/read/<key>/<tag>/')  
def read(key,tag):  
    res=redisClient.hget(key,tag)
    return res;  
@app.route('/write/<key>/<tag>/<value>/')  
def write(key,tag,value):  
    res=redisClient.hset(key, tag, value)
    return "data added successfully";  
  
if __name__ =='__main__':  
    app.run(debug = True)  