FROM python:3.10-slim-buster
WORKDIR /app

COPY ./basics /app/basics
COPY ./modules /app/modules

CMD ["python3", "-m", "basics.slice_string"]
