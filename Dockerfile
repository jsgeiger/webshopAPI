FROM python:3.7

COPY . .

WORKDIR /
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install mysqlclient
RUN pip install python-dotenv

CMD python ./run.py