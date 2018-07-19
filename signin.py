from flask import Flask,request,jsonify
import MySQLdb
db = MySQLdb.connect ('localhost','root','mutex','user')

app = Flask(__name__)

@app.route('/hello:',methods=['GET'])
def say_hello():
    data= request.args
    print data
    return "<h1>hello  "+data['username']+"  username="+data['surename']+\
            "  ::college="+data['college']+"</h1>"

@app.route ('/welcome')
def say_welcome():
    return "welcome"

@app.route('/bye')
def say_bye():
    return "bye"

@app.route('/goodbye')
def say_goodbye():
    return "goodbye"

@app.route('/login')
def login():
    data = request.args
    username = data['username']
    password = data['password']
    #mobileno = data['mobileno']
    cursor = db.cursor()
    query='select * from user where username=%s'
    cursor.execute("insert into user values(%s,%s)",[username,password]);
    db.commit()
    entry = cursor.fetchone()
    if not entry:
        return jsonify({"message":"invalid username!!"})
    if entry[1]==password:
       return jsonify({"message":"login seccessfull!!"})
    else:
      return jsonify({"message":"invalid password!!"})
    



if __name__=="__main__":
    app.run(host='localhost',port=2004,debug=True)
