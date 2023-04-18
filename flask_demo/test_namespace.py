from flask import Flask

from flask_restx import Namespace, Api, Resource

# 1.创建一个WSGI application
app = Flask(__name__)
api = Api(app)

# 2.实例化两个namespace
hello_ns = Namespace("demo", description="demo学习")
case_ns = Namespace("case", description="用例管理")


# 3.为类添加装饰器来控制子路由
@hello_ns.route("")
class TestCase(Resource):  # 类需要继承Resource
    def get(self):
        return {"code": 0, "msg": "get success"}

#4.为命令空间指定访问资源路径
api.add_namespace(hello_ns,"/case")

if __name__ == '__main__':
    app.run()