from flask import *  
import redis
app = Flask(__name__)  
  
@app.route('/write')  
def write():  
   return render_template('details.html')  

@app.route('/read')
def read():
    return render_template('get_details.html')

@app.route('/getvalue',methods = ['POST'])  
def get_data():  
   if request.method == 'POST':  
        result = request.form 
        key='EmployeeDetails' 
        tag=result['name']
        print(result['name'])
        redisclient=redis.Redis(host='127.0.0.1',port=6379)
        res=redisclient.hgetall(key)
        return 'The Phone Number is: '+str(res)

@app.route('/success',methods = ['POST'])  
def upload_data():  
   if request.method == 'POST':  
        result = request.form 
        key='EmployeeDetails' 
        tag=result['name']
        value=result['contact']
        print(result['name'])
        redisclient=redis.Redis(host='127.0.0.1',port=6379)
        redisclient.hset(key,tag,value)
        return render_template("result.html",result = result)  
  
if __name__ == '__main__':  
   app.run(debug = True)  