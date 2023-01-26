FROM python:3.9

WORKDIR /django_web

ENV DEBIAN_FRONTEND noninteractive

COPY . .
COPY requirements.txt ./
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

RUN pip install --upgrade pip
RUN pip install mysqlclient
RUN pip install -U pip wheel cmake
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000