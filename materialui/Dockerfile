FROM node:13.12.0-alpine as build_stage
# set working directory
WORKDIR /materialui

# add `/app/node_modules/.bin` to $PATH
ENV PATH /materialui/node_modules/.bin:$PATH
ENV NODE_ENV=production
ENV SKIP_PREFLIGHT_CHECK=true
EXPOSE 3000
# install react app dependencies
COPY package.json /materialui

RUN npm install
RUN npm install react-scripts@4.0.3 -g

# add client1
COPY . /materialui


# start app
#CMD ["npm", "start"]

#Run npm Build
RUN npm run build

# Stage 2
FROM nginx:1.17.1-alpine

RUN whoami
RUN apk add jq
RUN apk add --no-cache --upgrade bash

#RUN rm -rf /usr/share/nginx/html/*
COPY --from=build_stage /materialui/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000 80
#CMD while true; do sleep 1000; done
CMD ["nginx" , "-g" , "daemon off;"]

