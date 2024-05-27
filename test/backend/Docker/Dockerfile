FROM node:slim

WORKDIR /usr/src/app

COPY app.js ./

RUN chown -R node:node /usr/src/app

COPY package.json ./ 

RUN apt update && npm install

COPY --chown=node:node . .

EXPOSE 3000

CMD [ "node", "server.js"  ]
