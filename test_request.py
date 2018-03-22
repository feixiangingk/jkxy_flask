#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2017/11/12 18:25
# software:     PyCharm


import requests,time

class TestRequest():

    def __init__(self):
        self.s=requests.session()

    def test_index(self):
        URL='http://127.0.0.1:5000/index'
        headers={"client":"pycharm"}
        self.s.post(URL,headers=headers)

    def test_login(self):
        URL='http://127.0.0.1:5000/login'
        #带登录验证的post
        response=self.s.post(URL,auth=("gufan","123456"))
        print response.text

    def test_token(self):
        URL="http://127.0.0.1:5000/auth_token"
        token="Z3VmYW46MC4yMzIyNDMxMTA1OTg6MTUxNjc4MTA3Ny41OA=="
        response=self.s.get(URL,params={"token":token})
        print response.text

    def test_sc_flask(self):
        URL="http://11.8.37.144:5000/N009/entry"
        response=self.s.post(URL,data={"a":2})
        print response.text

if __name__=="__main__":
    test=TestRequest()
    # test.test_login()
    # test.test_token()
    test.test_sc_flask()



