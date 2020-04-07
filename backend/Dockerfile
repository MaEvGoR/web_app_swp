FROM python:3.7
ADD requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
ADD ./backend /code
WORKDIR /code
CMD python3 webapp.py