FROM python:3.7-alpine

# Delete packages after psycopg2 is installed 
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk del build-deps

WORKDIR /code

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY webapp.py /code
COPY backend /code/backend

# until they are removed from code:
COPY templates /code/templates

EXPOSE 5000

CMD ["python3", "webapp.py"]
