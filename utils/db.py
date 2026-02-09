import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True,
    setsession=[],
    ping=0,
    host='localhost', port=3306, user='root', passwd='123456', db='database', charset='utf8mb4'
)
# 如果连接服务器需要将host='localhost'改成host='mysql'


def fetch_one(sql, params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, params)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def fetch_all(sql, params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, params)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def execute(sql, args=None):
    """执行增删改操作（INSERT/UPDATE/DELETE），返回受影响行数"""
    conn = None
    cursor = None
    try:
        conn = POOL.connection()
        cursor = conn.cursor()
        affected_rows = cursor.execute(sql, args or ())
        conn.commit()  # 增删改必须提交事务
        return affected_rows
    except Exception as e:
        if conn:
            conn.rollback()  # 出错回滚
        print(f"执行增删改出错：{e}")
        raise e  # 抛出异常让上层处理
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()