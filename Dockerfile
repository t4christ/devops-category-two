FROM node:carbon-alpine 

WORKDIR usr/src/app

COPY package*.json ./

COPY bin/www ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "start"]
