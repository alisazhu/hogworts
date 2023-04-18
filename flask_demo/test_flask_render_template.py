import random

from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index():
#     title = 'python键值对'
#     author = 'alisa'
#     return render_template('index.html', var1=title, var2=author)
#
#
# @app.route('/')
# def index():
#     title = 'python键值对'
#     author = 'alisa'
#     return render_template('index.html', **locals())


# @app.route('/user')
# def user():
#     return render_template('user.html')

# @app.route('/user')
# def user():
#     return render_template('user.html',name='alisa')

# 在html中传递参数,其中url中存在可变参数时，需要在视图函数中对应中传入参数


# @app.route('/')
# def index():
#     """
#     html文件中带有if判断语句
#     :return:
#     """
#     name = random.randint(1,3)
#     return render_template('index_if.html', name=name)
#
#
# @app.route('/user/<username>')
# def user(username):
#     return render_template('user.html', name=username)


@app.route('/')
def index():
    goods = [
        {'name':"运动上衣","price":80},
        {'name':"西装上衣","price":100},
        {'name':"西装裤子","price":200}
    ]
    return render_template('goods.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
