FROM python:3.10-slim-buster
WORKDIR /app

COPY slice_string.py /app
COPY ./modules/string_slicing_module.py /app/modules/.

CMD ["python3","slice_string.py"]