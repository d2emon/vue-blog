FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 8080

RUN npm run build

CMD ["http-server", "dist"]
