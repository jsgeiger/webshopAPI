FROM python:3.7

COPY . .

WORKDIR /
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install mysqlclient
RUN pip install python-dotenv
RUN pip install email_validator

CMD python ./run.py