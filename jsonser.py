from flask import Flask,request,jsonify
import MySQLdb
db = MySQLdb.connect ('localhost','root','mutex','user')

app = Flask(__name__)

#@app.route('/hello:',methods=['GET'])
#def say_hello():
    #data= request.args
    #print data
    #return "<h1>hello  "+data['username']+"  username="+data['surename']+\
    #        "  ::college="+data['college']+"</h1>"

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
        return jsonify({"message":"invalid username!!"})
    if entry[1]==password:
       return jsonify({"message":"login seccessfull!!"})
    else:
      return jsonify({"message":"invalid password!!"})
    
@app.route('/signup')
def signup():
    data = request.args
    username = data['username']
    password = data['password']
    cursor = db.cursor()
    query = 'insert into user values(%s,%s)'
    cursor.execute(query, [username,password])
    db.commit()
    return "added"

@app.route('/fetchuser')
def fetchuser():
    data = request.args
    username = data['username']
    cursor = db.cursor()
    query = 'select password from user where username=%s'
    cursor.execute(query, [username])
    db.commit()
    entry = cursor.fetchone()
    if not entry:
        return jsonify({"message": "invalid username!!"})
    else:
        return entry

@app.route('/update')
def update():
    data = request.args
    username = data['username']
    #password = data['password']
    cursor = db.cursor()
    query = 'update user set password="xyz" where username=%s'
    cursor.execute(query, [username])
    db.commit()
    return "updated"


@app.route('/fetchall')
def fetchall():
    cursor = db.cursor()
    query = 'select * from user'
    cursor.execute(query)
    db.commit()
    entry = cursor.fetchall()
    u_dict={}
    list=[]
    for i in entry:
        u_dict={"username":i[0],"password":i[1]}
        list.append(u_dict)

    return jsonify({"user":list})

if __name__=="__main__":
    app.run(host='localhost',port=2007,debug=True)
