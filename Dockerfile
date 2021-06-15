FROM python:3.8-alpine
RUN apk --update add tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone
WORKDIR /data
CMD ["python","server.py"]
