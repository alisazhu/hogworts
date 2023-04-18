from flask import Flask, jsonify, render_template, make_response

from utils.log_utils import logger

app = Flask(__name__)


@app.route("/text")
def test_text():
    logger.info("响应返回文本信息")
    return "你好"


@app.route("/tuple")
def test_tuple():
    logger.info("响应返回tuple信息")
    return "你好", 200,{"code": 0, "msg": "success"}


@app.route("/json")
def test_json():
    logger.info("响应返回json")
    # return {"code": 0, "msg": "success"}
    return jsonify(code=0,msg="success",name="alisa")


@app.route("/html")
def test_html():
    # logger.info("")
    rep =make_response(render_template('demo.html'))
    rep.headers = {"name":"alisa"}
    return rep


if __name__ == '__main__':
    app.run(debug=True)
