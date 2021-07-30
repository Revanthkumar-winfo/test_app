
import connexion
import datetime
import logging
import redis
import connexion
from flask import *
import os

def login():
    return render_template('login.html')  
def read(key,tag): 
    redisClient = redis.Redis(
    host='127.0.0.1',
    port=6379) 
    res=redisClient.hget(key,tag)
    return "The value is"+str(res);  

def write(key,tag,value):
    redisClient = redis.Redis(
    host='127.0.0.1',
    port=6379)  
    res=redisClient.hset(key, tag, value)
    return "data added successfully"

app = connexion.App(__name__)
app.add_api("swagger.yml")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    
