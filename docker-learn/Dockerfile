FROM node:alpine as aliasprojbuild
WORKDIR /var/app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx
EXPOSE 80
COPY --from=aliasprojbuild /var/app/build /usr/share/nginx/html

