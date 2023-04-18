from flask import Flask

from utils.log_utils import logger

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


@app.route('/login', methods=['get'])
def get_method():
    logger.info('这是get方法')
    return {"code": 0, "msg": "get success"}


@app.route('/login', methods=['post'])
def post_method():
    logger.info('这是post方法')
    return {"code": 0, "msg": "post success"}


@app.route('/login', methods=["put"])
def put_method():
    logger.info('这是put方法')
    return {"code": 0, "msg": "put success"}


@app.route('/login', methods=['delete'])
def delete_method():
    logger.info('这是delete方法')
    return {"code": 0, "msg": "delete success"}


if __name__ == '__main__':
    app.run(debug=True)
