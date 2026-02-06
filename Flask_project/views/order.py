from flask import Blueprint, session, redirect, render_template

from utils import db

od = Blueprint('order', __name__)


@od.route('/order/list')
def order_list():
    user_info = session.get('user_info')
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

    return render_template("order_list.html", data_list=data_list, status_dict=status_dict,
                           real_name=user_info.get('real_name'))


@od.route('/order/create')
def create_order():
    return render_template('order_create.html')


@od.route('/order/delete')
def delete_order():
    return "删除订单"