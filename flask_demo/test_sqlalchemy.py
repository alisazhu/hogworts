from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.app_context().push()

# 数据库用户名
username = "root"
# 数据库密码
pwd = "123456"
# # 数据库ip
# ip = '192.168.80.21'
# # 数据库端口
# port = "8888"

server = "192.168.80.21:8888"
# 数据库名
database = "mysql"
# 设置数据库的连接方法为SQLALCHEMY_DATABASE_URI方式
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{pwd}@{server}/{database}"

# 追踪对象的修改，不配置时会抛出警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 将app与Flask-SQLAlchemy的db进行绑定，实例化一个数据库对象
db = SQLAlchemy(app)


# 定义一个类表示一张表,其中db.model表示这是一个数据库类型的类
# class Student(db.Model):
#     # 表中的属性使用Column()
#     id = Column(Integer, primary_key=True)
#     stu_username = Column(String(80))
#
#
# class Teacher(db.Model):
#     # 表中的属性使用Column()
#     id = Column(Integer, primary_key=True)
#     stu_username = Column(String(80))
#
#
#
# class Userinfo(db.Model):
#     # 表中的属性使用Column()
#     id = Column(Integer, primary_key=True)
#     stu_username = Column(String(80))
#
#
# class Classinfo(db.Model):
#     # 表中的属性使用Column()
#     id = Column(Integer, primary_key=True)
#     stu_username = Column(String(80))
#
#
# class TeacherInfo(db.Model):
#     # 表中的属性使用Column()
#     id = Column(Integer, primary_key=True)
#     stu_username = Column(String(80))


class SubTeacherInfo(db.Model):
    __tablename__ = 'subteacher_info'
    # 表中的属性使用Column()
    id = Column(Integer, primary_key=True)
    stu_username = Column(String(80))
    stu_member = Column(Integer, unique=True)


if __name__ == '__main__':
    # 创建表
    # db.create_all()

    # #实例化类，创建一个表对象
    # subteacher_info = SubTeacherInfo(id=3,stu_username='alisa',stu_member=4)
    #
    # #将实例添加到数据库的session中
    # db.session.add(subteacher_info)
    #
    # #提交实例
    # db.session.commit()
    #
    # #关闭session
    # db.session.close()

    # 多次实例化类，创建多个表数据
    # sub_info_1 = SubTeacherInfo(id=4,stu_username='daqiang', stu_member=5)
    #     # sub_info_2 = SubTeacherInfo(id=5,stu_username='xiaozhu', stu_member=1)
    #     #
    #     # # 将创建的对象全部添加到session中,add_all()方法中传入的是一个可迭代的列表
    #     # db.session.add_all([sub_info_1,sub_info_2])
    #     #
    #     # # 提交session对象
    #     # db.session.commit()
    #     #
    #     # # 关闭session
    #     # db.session.close()

    # res = SubTeacherInfo.query.all()
    # res = SubTeacherInfo.query.filter_by(id=1).filter_by(stu_username='alisa').first()
    # res.stu_username='afen'

    # es = SubTeacherInfo.query.filter_by(id=1)
    # print(es)
    #
    # res = SubTeacherInfo.query.filter_by(id=1).update({"stu_username":"afen"})
    #
    # print(res)
    # print(SubTeacherInfo.query.filter_by(stu_username='alisa').all())
    # # for re in res:
    #
    # #     print(re.stu_username,re.stu_member)
    #
    # # 删除表
    # # db.drop_all()
    #
    # # db.session.add(res)
    #
    # db.session.commit()
    #
    # db.session.close()

    # # 表中数据的删除
    # res = SubTeacherInfo.query.filter_by(id=1).first()
    #
    # # 删除数据对象
    # db.session.delete(res)
    #
    # # 提交session
    # db.session.commit()
    #
    # # 关闭session
    # db.session.close()

    # 查询后直接进行delete操作
    SubTeacherInfo.query.filter_by(id=11).delete()

    db.session.commit()

    db.session.close()
