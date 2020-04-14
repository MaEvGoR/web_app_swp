FROM node:13-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install
ENV PATH /app/node_modules/.bin:$PATH
ADD . /app/src
WORKDIR /app/src

EXPOSE 3000

RUN npm run build
CMD npm run serve