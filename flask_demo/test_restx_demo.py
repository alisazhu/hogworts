from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)


# 定义一个类来实现函数,其中类要继承Resource模块
@api.route("/login","/login1")
class LoginIn(Resource):
    #将需要实现的方法编写在类内
    def get(self):
        return {"code": 0, "msg": "success"}

    def post(self):
        return {"code": 0, "msg": "success"}

    def put(self):
        return {"code": 0, "msg": "success"}

    def delete(self):
        return {"code": 0, "msg": "success"}


api.add_resource(LoginIn,"/login","/login1")



if __name__ == '__main__':
    app.run(debug=True)