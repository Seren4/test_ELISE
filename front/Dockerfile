FROM node:9

RUN mkdir -p /app
WORKDIR /app

COPY ./app/package.json ./

RUN npm i npm@latest -g
RUN npm install -g @vue/cli

RUN npm install -qy

ENV PATH /app/node_modules/.bin:$PATH

EXPOSE 8080

CMD ["npm", "run", "serve"]
