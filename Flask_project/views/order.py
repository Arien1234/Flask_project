from flask import Blueprint, session, redirect, render_template, request, url_for
import pymysql
from utils import db

od = Blueprint('order', __name__)


@od.route('/order/list')
def order_list():
    user_info = session.get('user_info')
    # 获取创建订单成功的提示信息
    success_msg = request.args.get('success')

    role = user_info.get('role')
    if role == 2:
        data_list = db.fetch_all("select * from `order` left join user on `order`.`user_id` = `user`.`id`", [])
    else:
        data_list = db.fetch_all(
            "select * from `order` left join user on `order`.`user_id` = `user`.`id` where `order`.user_id=%s",
            [user_info.get('id')], )
    print(data_list)

    status_dict = {
        1: "待执行",
        2: "正在执行",
        3: "完成",
        4: "失败",
    }

    return render_template("order_list.html",
                           data_list=data_list,
                           status_dict=status_dict,
                           real_name=user_info.get('real_name'),
                           success=success_msg)  # 传递成功提示


@od.route('/order/create', methods=['GET', 'POST'])
def create_order():
    user_info = session.get('user_info')
    # 检查用户是否登录（补充缺失的登录校验）
    if not user_info:
        return redirect('/login')

    # GET请求：展示创建订单表单
    if request.method == 'GET':
        return render_template('order_create.html', user_info=user_info)

    # POST请求：处理订单创建
    try:
        # 获取表单数据
        url = request.form.get('url').strip()
        count = request.form.get('count')

        # 基础校验
        if not url or not count:
            return render_template('order_create.html',
                                   user_info=user_info,
                                   error="URL和数量均为必填项！")

        # 转换数量为整数
        try:
            count = int(count)
            if count < 1:
                return render_template('order_create.html',
                                       user_info=user_info,
                                       error="数量必须大于0！")
        except ValueError:
            return render_template('order_create.html',
                                   user_info=user_info,
                                   error="数量必须为有效数字！")

        # 获取当前用户ID
        user_id = user_info['id']
        # 订单状态默认设为1
        status = 1

        # 插入订单数据到数据库
        db.execute(
            "insert into `order` (url, count, user_id, status) values (%s, %s, %s, %s)",
            (url, count, user_id, status)
        )

        # 注册成功，跳转到订单列表页并携带成功提示
        return redirect(f"/order/list?success=订单创建成功！")

    except pymysql.MySQLError as e:
        # 数据库异常处理
        return render_template('order_create.html',
                               user_info=user_info,
                               error=f"订单创建失败：{str(e)}")
    except Exception as e:
        # 其他异常处理
        return render_template('order_create.html',
                               user_info=user_info,
                               error=f"系统错误：{str(e)}")


@od.route('/order/delete')
def delete_order():
    return "删除订单"