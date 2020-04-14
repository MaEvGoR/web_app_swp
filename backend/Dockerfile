FROM python:3.7
ADD requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
ADD ./backend /code
WORKDIR /code

EXPOSE 5000

CMD python3 webapp.py