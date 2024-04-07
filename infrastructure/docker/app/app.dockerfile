FROM node:14 as Base

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --ignore-engines

COPY . ./

RUN npx prisma && npx prisma generate

RUN yarn build

FROM node:14

WORKDIR /app

COPY --from=Base /app .

RUN chmod +x entrypoint.sh

EXPOSE 8080

# Sets the command and parameters that will be executed first when a container is ran.
ENTRYPOINT "./entrypoint.sh"