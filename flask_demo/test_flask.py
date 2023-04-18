from flask import Flask, url_for, redirect

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '这是url传参演示'


# @app.route('/hello/<name>')
# def hello(name):
#     return "接收到的名称为%s" % name
#
#
# # url反转，这里的id可以是动态变化的吗
# @app.route('/')
# def index():
#     # url_for传参的第一个参数是视图函数的引用，返回对应的url，第二个参数是在url后面拼接的参数
#     url1 = (url_for('news', id='10086'))
#     return f"返回的url是{url1}"
#
#
# @app.route('/newsaad/<int:id>')
# def news(id):
#     return "接收到的id是%s" % id

# @app.route('/')
# def index():
#     #反转url，指向对应视图函数的url
#     url1 = url_for('user_login')
#
#     # 将url1重定向，之后将重定向的结果返回,因为redirect()函数返回的是一个响应对象
#     # 这个对象被调用时，会将客户端重新定向到目标位置，所以如果不返回这个对象时，相当于没有调用这个对象，那么就不会进入重新定向的页面
#     url2 = redirect(url1)
#     return url2
#
#
# @app.route('/user/login')
# def user_login():
#     return "这是登录页面"


@app.route('/')
def index():
    url1 = url_for('my_list')
    return f'反转url地址是{url1}'


@app.route('/list/')
def my_list():
    return 'list'


if __name__ == '__main__':
    app.run(debug=True)
