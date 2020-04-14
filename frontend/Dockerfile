FROM node:13-alpine

RUN mkdir -p /app

WORKDIR /app

COPY package.json /app/
RUN npm install

ADD . /app

EXPOSE 8080

CMD npm run serve
