# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制Python脚本到容器中
COPY mail_sender.py /app/

# 设置默认命令
CMD ["python", "mail_sender.py"]