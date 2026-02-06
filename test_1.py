# import pymysql
# from pymysql.err import OperationalError, ProgrammingError
#
#
# def query_user_by_params(role, mobile, password):
#     db_config = {
#         'host': 'localhost',  # 数据库主机地址
#         'port': 3306,  # 数据库端口
#         'user': 'root',  # 数据库用户名
#         'password': '123456',  # 数据库密码（替换为你的实际密码）
#         'db': 'database',  # 数据库名（替换为你的实际数据库名）
#         'charset': 'utf8mb4'  # 字符集（支持中文等特殊字符）
#     }
#
#
#     conn = None
#     cursor = None
#     try:
#         # 3. 建立数据库连接
#         conn = pymysql.connect(**db_config)
#         # 4. 创建游标（指定cursorclass，查询结果以字典格式返回，更易读取）
#         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
#         # 5. 定义SQL语句（%s是pymysql的参数占位符，与Python字符串格式化的%s无关）
#         sql = "SELECT * FROM user WHERE role=%s AND mobile=%s AND password=%s"
#
#         # 6. 执行参数化查询（第二个参数是元组格式的参数列表，必须与SQL中的%s一一对应）
#         # 重点：参数必须以元组传入，即使只有一个参数也要加逗号（如(role,)）
#         cursor.execute(sql, (role, mobile, password))
#
#         # 7. 获取查询结果（fetchall()获取所有匹配记录，fetchone()获取单条记录）
#         query_result = cursor.fetchall()
#
#         return query_result
#
#     except OperationalError as e:
#         print(f"数据库连接失败或操作异常：{e}")
#         return None
#     except ProgrammingError as e:
#         print(f"SQL语句错误或表/字段不存在：{e}")
#         return None
#     finally:
#         # 8. 关闭游标和连接（无论成功与否，都要释放资源）
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()
#
# if __name__ == "__main__":
#     # 传入三个查询参数（替换为你要查询的实际值）
#     target_role = "admin"
#     target_mobile = "13812345678"
#     target_password = "123456abc"
#
#     # 调用函数执行查询
#     user_info = query_user_by_params(target_role, target_mobile, target_password)
#
#     # 打印查询结果
#     if user_info:
#         print(f"查询到 {len(user_info)} 条匹配记录：")
#         for user in user_info:
#             print(user)
#     else:
#         print("未查询到匹配记录，或查询过程出现异常。")

print('hello world')
def auth():
    print('hello world')
