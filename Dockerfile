FROM python:3
WORKDIR /app
COPY map.py /app


CMD ["python3","map.py"]