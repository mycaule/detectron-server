FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY configs /app/configs
COPY utils /app/utils
COPY requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# TODO Install detectron2 from GitHub

COPY . /app
