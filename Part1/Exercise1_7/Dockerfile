#  starts from ubuntu:20.04 
FROM ubuntu:20.04

# Copy website.sh
COPY website.sh .

# add instructions to install curl into that image
RUN apt update; apt install -y curl

# add instructions to copy the script file into that image
CMD ./website.sh
