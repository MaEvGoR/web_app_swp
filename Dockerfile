FROM python:3.7
ADD requirements.txt /code
RUN pip3 install -r requirements.txt
ADD . /code
WORKDIR /code
CMD python3 webapp.py