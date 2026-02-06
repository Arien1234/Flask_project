# 基础镜像（和本地Python版本一致，如3.9）
FROM python:3.9-slim

# 容器内工作目录（自定义，如/app）
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖（CentOS下同样可用阿里云源加速）
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 复制所有项目文件
COPY . .

# 暴露端口（和app.py的port一致，如5000）
EXPOSE 5000

# 启动命令（指向你的app.py，工厂模式无需改）
CMD ["python", "app.py"]