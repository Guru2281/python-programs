from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return "hello"

@app.route ('/welcome')
def say_welcome():
    return "welcome"

@app.route('/bye')
def say_bye():
    return "bye"

@app.route('/goodbye')
def say_goodbye():
    return "goodbye"



if __name__=="__main__":
    app.run(host='localhost',port=2004,debug=True)
