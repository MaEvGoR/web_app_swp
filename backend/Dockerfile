FROM python:3.7
 
WORKDIR /code

ADD requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY webapp.py /code
COPY backend /code/backend

# until they are removed from code:
COPY templates /code/templates

EXPOSE 5000

CMD ["python3", "webapp.py"]
