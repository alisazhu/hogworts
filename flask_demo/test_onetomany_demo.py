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


# 班级表
class ClassInfo(db.Model):
    __tablename__ = 'Class'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    def __repr__(self):
        return f"<Class:{self.name}>"


# 学生表
class StudentInfo(db.Model):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    # 添加外键，建立学生表和班级表之间的关联,这里是将需要在表中添加外键的id进行重命名
    classid = Column(Integer, ForeignKey("Class.id"))

    # 完成两个数据表之间的映射，从而达到查表的信息，其中第一个参数是需要查的表代表的类名，第二个参数是backref建立类ClassInfo声明属性的一种新的方法
    class_info = db.relationship("ClassInfo", backref='student_info')

    def __repr__(self):
        return f"<Student:{self.name}>"


if __name__ == '__main__':
    # 1.先实例化类创建表对象

    # class表添加数据
    # class_1 = ClassInfo(id=1, name='英语第一期')
    # class_2 = ClassInfo(id=2, name='英语第二期')
    #
    # # student表添加数据,也需要指定外键的值，外键的值需要在另外一张表中存在
    # student_1 = StudentInfo(id=1, name='alisa', classid=1)
    # student_2 = StudentInfo(id=2, name='daqiang', classid=2)
    #
    # # 2.将实例添加到数据库的session中，参数是一个列表
    # db.session.add_all([class_1, class_2, student_1, student_2])
    #
    # # 3.提交session
    # db.session.commit()
    #
    # # 关闭session
    # db.session.close()

    # 创建表
    # db.create_all()

    # db.drop_all()

    # 查询操作---查询学生id=1所在的班级信息
    # 查询方法：1.通过学生id获取该学生的班级id，通过班级id查询班级信息
    # stu1 = StudentInfo.query.filter_by(id=1).first()
    #
    # print(stu1.classid)
    #
    # # 打印对应的信息
    # print(stu1.class_info.name)

    # 查询操作----查询班级id=1学生的信息

    # 查询方法：1.通过班级id反向引用student_info

    # class1 = ClassInfo.query.filter_by(id=1).first()
    # print(class1.student_info)
    #
    # print(class1.student_info[0].id)

    # #一该多：改动班级中学生的信息
    #
    # class1 = ClassInfo.query.filter_by(id=1).first()
    # print(class1.student_info)
    # class1.student_info[0].name = 'alisa1'
    #
    # db.session.commit()
    # db.session.close()

    # # 多改一：改动学生对应的班级信息
    # stu1 = StudentInfo.query.filter_by(id=1).first()
    #
    # print(stu1.class_info.name)
    # stu1.class_info.name = '英语第2期'
    #
    # db.session.commit()
    # db.session.close()

    # 一删多,通过班级查出来学生的id，在学生表中删除对应的学会信息

    # 1.通过class_id查询出对应的班级
    class1 = ClassInfo.query.filter_by(id=2).first()

    print(class1.student_info)

    # 在学生表中查询学生class_id，如何和班级id相同，则在student表删除学生的信息
    print(StudentInfo.query.filter(StudentInfo.classid == class1.id))

    # 删除操作
    StudentInfo.query.filter(StudentInfo.classid == class1.id).delete()

    db.session.commit()

    db.session.close()

    print(StudentInfo.query.all())
