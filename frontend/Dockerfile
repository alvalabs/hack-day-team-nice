FROM node:12-alpine3.9 as develop
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn
COPY . .

FROM develop as build
RUN yarn build

FROM nginx:mainline-alpine as prod
WORKDIR /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx-conf/* /etc/nginx/conf.d/
COPY --from=build /app/build/ .
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]