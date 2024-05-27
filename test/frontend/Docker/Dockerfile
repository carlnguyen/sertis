FROM node:slim

WORKDIR /app

COPY package.json /app

RUN apt update

EXPOSE 8080

CMD [ "node", "server.js"  ]
