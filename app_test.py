
import connexion
import datetime
import logging
import redis
import connexion
from flask import *
import os
from py2neo import Graph
import pandas

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

def neo4j_read(relation,name):
    graph = Graph("http://localhost:7474", auth=("neo4j", "Winfo_123"))
    df=graph.run("MATCH (a:"+relation+") RETURN a."+name)
    return json.dumps(df)

def neo4j_write(node,property,value):
    graph = Graph("http://localhost:7474", auth=("neo4j", "Winfo_123"))
    graph.run("CREATE (a:"+node+") SET a."+property+" = '"+value+"'").stats()
    return "Data Added Successfully"


app = connexion.App(__name__)
app.add_api("swagger.yml")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    
