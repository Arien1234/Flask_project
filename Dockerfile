# 基础镜像：Python 3.11 轻量版（兼容大部分 Flask 项目）
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件，利用 Docker 缓存（先装依赖再复制代码，提速）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制所有项目代码到容器
COPY . .

# 暴露端口（和 app.py 里的 5000 对应）
EXPOSE 5000

# 生产环境启动命令（用 gunicorn 替代直接运行）
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "2"]