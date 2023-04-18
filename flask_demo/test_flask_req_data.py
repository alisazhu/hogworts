from flask import Flask, request

from utils.log_utils import logger

app = Flask(__name__)


@app.route('/login', methods=["get"])
def user_login():
    result = request.args
    username = result.get("username")
    password = result.get("password")
    logger.info(f"传递的用户名是{username},传递的密码是{password}")

    return {"code": 0, "msg": "get success"}


@app.route('/regist', methods=['post'])
def user_regist():
    result = request.json
    username = result.get("username")
    password = result.get("password")

    logger.info(f"传递的用户名是{username},传递的密码是{password}")

    return {"code": 0, "msg": "post success"}


@app.route('/confirm', methods=["post"])
def user_confirm():
    result = request.form
    username = result.get("username")
    password = result.get("password")

    logger.info(f"传递的用户名是{username},传递的密码是{password}")

    return {"code": 0, "msg": "post success"}


@app.route('/avatar', methods=["post"])
def user_avatar():
    result = request.files
    # 获取的是一个文件对象
    fileobj = result.get("file")
    method = request.method
    path = request.path
    logger.info(f"获取到的文件对象为{fileobj}")
    logger.info(f"请求的方法为{method}")
    logger.info(f"请求的路径为{path}")

    fileobj.save('./day.png')

    return {"code": 0, "msg": "post success"}


if __name__ == '__main__':
    app.run(debug=True)
