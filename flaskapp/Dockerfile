FROM ubuntu

RUN apt-get update
RUN apt-get install python python-pip -y
RUN pip install flask

COPY hello.py /opt/hello.py

ENTRYPOINT FLASK_APP=/opt/hello.py flask run --host='0.0.0.0'
EXPOSE 5000
