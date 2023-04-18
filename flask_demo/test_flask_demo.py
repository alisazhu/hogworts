from flask import Flask


# __name__是应用包名，一般情况下使用当前的模块
from utils.log_utils import logger

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/alisa')
def hello_alisa():
    return "你好，Alisa，我是flask"


@app.route('/hello/<int:username>')
def hello_user(username):
    logger.info("动态路由设置对应的变量格式")
    return f'hello{username} '




if __name__ == '__main__':
    # 运行程序
    app.run(debug=True)
