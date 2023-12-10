#  starts from java 8 
FROM openjdk:8

EXPOSE 8080

# setting the workdir and copying the content 
WORKDIR /usr/src/app
COPY . .

# Build the project
RUN ./mvnw package

# Execute project 
CMD ["java","-jar", "./target/docker-example-1.1.3.jar"]
