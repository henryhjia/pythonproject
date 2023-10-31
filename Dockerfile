FROM python:3
WORKDIR /app
COPY slice_string.py /app
COPY ./modules/string_slicing_module.py /app

CMD ["python3","slice_string.py"]