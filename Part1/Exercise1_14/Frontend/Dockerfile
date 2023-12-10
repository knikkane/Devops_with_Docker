#  starts from ubuntu:20.04 
FROM ubuntu:20.04
EXPOSE 5000

# setting the workdir and copying the content 
WORKDIR /usr/src/app
COPY . .

# add instructions to install curl into that image
RUN apt update; apt install -y curl

# Prerequisites
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash
RUN apt install -y nodejs

# Exercise 1.14 -> to connect to backend
ENV REACT_APP_BACKEND_URL=http://localhost:8080

# Install all packages
RUN npm install
# Build the static files
RUN npm run build
# Install all packages with `npm install`
RUN npm install -g serve

# command to run the application
CMD ["serve", "-s", "-l", "5000", "build"]
