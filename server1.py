from flask import Flask, request
import MySQLdb


db = MySQLdb.connect ('localhost','root','mutex','user')

app = Flask(__name__)

@app.route('/hello:',methods=['GET'])
def say_hello():
    data= request.args
    print(data)
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
    cursor = db.cursor()
    query='select *from user where username=%s'
    cursor.execute(query,[username])
    db.commit()
    entry = cursor.fetchone()
    if not entry:
        return "invalid username!!"
    if entry[1]==password:
        return "logine successfull!!!"
    else:
        return"invalid password!!!!"
    



if __name__=="__main__":
    app.run(host='localhost',port=2005,debug=True)
