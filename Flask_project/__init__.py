from flask import Flask, request, session, redirect

# 拦截
def auth():
    # 放行静态资源
    if request.path.startswith('/static'):
        return

    # 放行登录页面和注册页面
    if request.path in ('/login', '/register'):
        return

    # 检查用户登录状态
    user_info = session.get('user_info')
    if user_info:
        return

    # 未登录则重定向到登录页
    return redirect('/login')


def create_app():
    app = Flask(__name__)
    app.secret_key = 'adkagkwyiya24154gwdawd'

    from .views import account
    from .views import order
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)

    app.before_request(auth)
    return app
