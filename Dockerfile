FROM python:3.8
COPY Log/ /data/
WORKDIR /data
CMD ["python","server.py"]