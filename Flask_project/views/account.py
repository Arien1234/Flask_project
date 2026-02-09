from flask import Blueprint, render_template, request, redirect, session
from utils import db
import pymysql

ac = Blueprint('account', __name__)


# 登录逻辑（移除密码加密）
@ac.route('/login', methods=['GET', 'POST'])
def login():
    success_msg = request.args.get('success')
    if request.method == 'GET':
        return render_template("login.html", success=success_msg)

    role = request.form.get('role')
    mobile = request.form.get('mobile')
    pwd = request.form.get('pwd')

    # 直接使用原始密码查询，不再加密
    user_dict = db.fetch_one(
        "select * from user where role = %s and mobile = %s and password = %s",
        (role, mobile, pwd)
    )
    if user_dict:
        session["user_info"] = {
            'role': user_dict['role'],
            'real_name': user_dict['real_name'],
            'id': user_dict['id']
        }
        return redirect('/order/list')
    return render_template("login.html", error="手机号或密码错误", success=success_msg)


# 注册逻辑（移除密码加密）
@ac.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    # 1. 获取表单提交的数据
    role = request.form.get('role')
    real_name = request.form.get('real_name')
    mobile = request.form.get('mobile')
    pwd = request.form.get('pwd')

    # 2. 基础校验
    if not all([role, real_name, mobile, pwd]):
        return render_template("register.html", error="所有字段均为必填项！")

    # 校验手机号长度
    if len(mobile) != 11:
        return render_template("register.html", error="手机号必须为11位！")

    # 3. 检查手机号是否已存在
    exists_user = db.fetch_one(
        "select id from user where mobile = %s",
        (mobile,)
    )
    if exists_user:
        return render_template("register.html", error="该手机号已注册！")

    try:
        # 插入数据到数据库（省略id字段，由数据库自增生成）
        db.execute(
            "insert into user (mobile, password, real_name, role) values (%s, %s, %s, %s)",
            (mobile, pwd, real_name, role)
        )

        # 注册成功，跳转到登录页并携带成功提示
        return redirect(f"/login?success=注册成功！请登录")

    except pymysql.MySQLError as e:
        # 数据库异常捕获
        return render_template("register.html", error=f"注册失败：{str(e)}")


# 原有users路由（不变）
@ac.route('/users')
def users():
    return "users page"