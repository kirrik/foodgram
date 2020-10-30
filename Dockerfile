FROM python:3.8

WORKDIR /code
COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY . .