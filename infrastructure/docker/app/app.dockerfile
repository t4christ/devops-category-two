FROM node:14 as Base

ARG UID=65534
ARG GID=65534


WORKDIR /app

COPY package.json ./

RUN yarn install --ignore-engines

COPY . ./

RUN npx prisma && npx prisma generate

RUN yarn build && chown -R ${UID}:${GID} dist

FROM node:14-alpine

ARG UID=65534
ARG GID=65534

WORKDIR /app

COPY --from=Base /app .

RUN chmod +x entrypoint.sh

USER ${UID}:${GID}

EXPOSE 8080

# Sets the command and parameters that will be executed first when a container is ran.
ENTRYPOINT "./entrypoint.sh"