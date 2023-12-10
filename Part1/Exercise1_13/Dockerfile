#  starts from golang 1.16 
FROM golang:1.16

EXPOSE 8080

# setting the workdir and copying the content 
WORKDIR /usr/src/app
COPY . .

# Build project
# RUN go build 

# Test project
# RUN test ./...

# Environment variables in 1.12 and after
# ENV REQUEST_ORIGIN=http://localhost:5000

RUN go build

# Execute project 
CMD ["./server"]
