FROM python:3.9-slim

# 更换阿里云源
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

# 安装编译依赖
RUN apt-get update -o Acquire::Timeout=300 && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    libssl-dev \
    libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装（追加 DBUtils）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn cryptography pymysql DBUtils -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目代码
COPY . .

# 启动Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]