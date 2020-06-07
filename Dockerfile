FROM python:3.7

WORKDIR /
COPY ./requirements.txt /requirements.txt
COPY ./run.py /run.py
RUN pip install -r /requirements.txt
RUN pip install mysqlclient
RUN pip install python-dotenv
RUN pip install email_validator

CMD python ./run.py