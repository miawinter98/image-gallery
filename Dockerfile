FROM ghcr.io/rtsp/docker-lighttpd:1.4.73 AS base
ARG BASE='/'
EXPOSE 80

FROM node:lts-alpine AS dependencies
WORKDIR /src/
COPY . .
RUN npm ci

FROM dependencies AS build
WORKDIR /src/
RUN npx astro build \
    --base $BASE

FROM base AS deploy
COPY --from=build /src/dist/ /var/www/html
