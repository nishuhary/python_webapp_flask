FROM ubuntu

RUN apt-get update
RUN apt-get install -y python 
RUN apt-get install -y python3-pip
RUN pip3 install flask flask-mysql
COPY app.py /opt/app.py
WORKDIR /opt
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0