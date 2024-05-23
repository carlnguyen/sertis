FROM node:20

WORKDIR /app

COPY package.json /app

RUN apt update && apt upgrade -y && npm install

COPY *.js /app

EXPOSE 8080

CMD [ "node", "server.js"  ]
