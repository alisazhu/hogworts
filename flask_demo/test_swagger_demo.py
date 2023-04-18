from flask import Flask, request
from flask_restx import Resource, Api, Namespace, fields
from werkzeug.datastructures import FileStorage

from utils.log_utils import logger

app = Flask(__name__)
api = Api(app, version=1.1)

hello_ns = Namespace("hello_ns", description="login接口方法")


@hello_ns.route('')
class TestCase(Resource):
    # @hello_ns.doc(params={'id':"An Id"})
    # def get(self):
    #     return {"code":0,"msg":"get success"}
    #
    # """
    # post方法中添加参数，使用api.model进行添加参数
    # """
    # post_model = api.model('PostModel',{
    #     'name':fields.String(description='The name',required=True)
    # })
    #
    # @hello_ns.doc(body=post_model)
    # def post(self):
    #     return {"code":0,"msg":"get success"}

    get_parser = api.parser()
    get_parser.add_argument('id', type=int, location='args')
    get_parser.add_argument('case_title', type=str, location="args")

    @hello_ns.expect(get_parser)
    def get(self):
        logger.info(f"request.args====>{request.args}")
        return {"code": 0, "msg": "get success"}

    post_parser = api.parser()
    post_parser.add_argument('name', type=str, location='json',required=True)
    post_parser.add_argument('addr',type=str,location='json',required=True)
    post_parser.add_argument('file',type=FileStorage,location='files')
    post_parser.add_argument('gender',choices=('man','female'),location='args')
    post_parser.add_argument('param1',type=int,help='username',location='form')
    post_parser.add_argument('param2',type=int,help='password',location='form')

    @hello_ns.expect(post_parser)
    def post(self):
        logger.info(f"request.args===>{request.args}")
        logger.info(f"request.args===>{request.form}")
        logger.info(f"request.args===>{request.json}")
        logger.info(f"request.args===>{request.files}")
        return {"code": 0, "msg": "post success"}



api.add_namespace(hello_ns, "/login")

if __name__ == '__main__':
    app.run(debug=True)
