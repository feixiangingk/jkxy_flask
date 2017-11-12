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
        token="Z3VmYW46MC43MTUwNTQ1Mjk5NzY6MTUxMDUwNjIwMS44NQ=="
        response=self.s.get(URL,params={"token":token})
        print response.text

if __name__=="__main__":
    test=TestRequest()
    # test.test_login()
    test.test_token()



    #
    # t1=time.time()
    # time.sleep(1)
    # t2=time.time()
    # print float(t1),float(t2),float(t2)>float(t1)