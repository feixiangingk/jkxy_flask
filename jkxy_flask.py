#coding:utf-8
from flask import Flask,request,render_template,g
app = Flask(__name__)
import base64,random,time,urllib


user={"username":"gufan","pwd":"123456"}
# @app.before_request
# def set_up_data():
#     g.user={"username":"gufan","pwd":"123456"}

def get_token(uid):
    token=base64.b64encode(":".join([str(uid),str(random.random()),str(time.time()+7200)]))
    user.update({"token":token})
    return token

def verify_token(token):
    _token=base64.b64decode(token)

    print float(_token.split(":")[-1]),float(time.time())
    if user.get("token",None)!=token:
        return -1
    if float(_token.split(":")[-1])>=float(time.time()):
        return 1
    else:
        print "time out"
        return 0

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/index",methods=["POST","GET"])
def index():
    print request.headers
    return "i'm index route~"

@app.route("/login",methods=['POST'])
def login():
    encrypt_code=request.headers['Authorization'].split(" ")[-1]
    decrypt_code=base64.b64decode(encrypt_code)
    username,pwd=decrypt_code.split(":")
    print username,pwd
    if username==user["username"] and pwd==user["pwd"]:
        print "login!"
        token=get_token(username)
        return token
    else:
        return "error"

@app.route("/auth_token",methods=["GET"])
def auth_token():
    token=request.args.get("token")
    print verify_token(token),"dddd"
    if verify_token(token)==1:
        return "verify success!"
    else:
        return "fail"

#返回指定状态码。以及headers
@app.route("/book14")
def book14():
    #可以返回一个元组，body | 状态码 | headers
    return "<h3>jkxy_bad request!</h3>",502,{"Accept": "application/xml;"}


if __name__ == '__main__':
    app.run(debug=True)
