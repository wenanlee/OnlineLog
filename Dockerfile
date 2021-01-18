FROM python:3.8-alpine
COPY Log/ /data/
WORKDIR /data
CMD ["python","server.py"]
