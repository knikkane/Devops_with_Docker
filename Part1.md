# Devops_with_Docker
# Part 1

## 1.1: GETTING STARTED
Start 3 containers from an image that does not automatically exit (such as nginx) in detached mode.

```shell
~$ docker image ls -a
REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
nginx           latest    a6bd71f48f68   10 days ago     187MB
```
```shell
~$ docker container run -d nginx
67c7e50835d38bda6a3e1a5bb54c2f2f189a22da0f6fd9d78c92334b6505e65a
~$ docker container run -d nginx
6b21610396b727b8664d888ed74a10328caacbd2dfab2be1571e9e193858b7ad
~$ docker container run -d nginx
ba1c1d1a7743776a6a36aba7005f88b29a80cf4de5cc59493c52080aabe93140
~$ docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS     NAMES
ba1c1d1a7743   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    competent_mclean
6b21610396b7   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    interesting_merkle
67c7e50835d3   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    infallible_williamson
~$ docker container stop 67c7e5
67c7e5
~$ docker container stop 6b2161
6b2161
~$ docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                      PORTS     NAMES
ba1c1d1a7743   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes                80/tcp    competent_mclean
6b21610396b7   nginx     "/docker-entrypoint.…"   2 minutes ago   Exited (0) 42 seconds ago             interesting_merkle
67c7e50835d3   nginx     "/docker-entrypoint.…"   2 minutes ago   Exited (0) 57 seconds ago             infallible_williamson
(base) kimmo@kimmo-ThinkPad-X1-Titanium-Gen-1:~$ 

```

## 1.2: CLEANUP
Clean the Docker daemon by removing all images and containers

```shell
~$ docker container ls
docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
ba1c1d1a7743   nginx     "/docker-entrypoint.…"   8 minutes ago   Up 8 minutes   80/tcp    competent_mclean
~$ docker container stop ba1c1d
ba1c1d
```
```shell
~$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
ba1c1d1a7743776a6a36aba7005f88b29a80cf4de5cc59493c52080aabe93140
6b21610396b727b8664d888ed74a10328caacbd2dfab2be1571e9e193858b7ad
67c7e50835d38bda6a3e1a5bb54c2f2f189a22da0f6fd9d78c92334b6505e65a
```
```shell
~$ docker image ls
REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
nginx           latest    a6bd71f48f68   10 days ago     187MB
~$ docker image prune -a
$ docker image prune -a
WARNING! This will remove all images without at least one container associated to them.
Are you sure you want to continue? [y/N] y
Deleted Images:
untagged: nginx:latest
```
```shell
~$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
~$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
~$ 
```

## 1.3: SECRET MESSAGE
Use tail -f ./text.log to follow the logs

```shell
~$ docker run -d --rm -it --name message devopsdockeruh/simple-web-service:ubuntu
~$ docker exec -it message bash
root@31ad3866446e:/usr/src/app# tail -f ./text.log
2023-12-01 15:22:47 +0000 UTC
2023-12-01 15:22:49 +0000 UTC
2023-12-01 15:22:51 +0000 UTC
2023-12-01 15:22:53 +0000 UTC
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
```

## 1.4: MISSING DEPENDENCIES
Install Curl, start a Ubuntu image with the process with sh -c 'while true; do echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website; done'
Test inputting helsinki.fi into the application

```shell
~$ docker run -d -it --name website ubuntu /bin/bash
~$ docker exec -d -it website /bin/bash -c 'apt update; apt install -y curl; exec "$BASH"'
```

```shell
~$ docker exec -it website /bin/bash -c 'echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website;'
Input website:
helsinki.fi
Searching..
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.22.1</center>
</body>
</html>
```

## 1.5: SIZES OF IMAGES
Compare the image sizes

```shell
~$ docker image ls
REPOSITORY                          TAG       IMAGE ID       CREATED       SIZE
devopsdockeruh/simple-web-service   ubuntu    4e3362e907d5   2 years ago   83MB
devopsdockeruh/simple-web-service   alpine    fd312adc88e0   2 years ago   15.7MB
```

## 1.6: HELLO DOCKER HUB
Go inside the alpine container and make sure the secret message functionality is the same.

```shell
~$ docker run -d --rm -it --name message devopsdockeruh/simple-web-service:alpine
d8c027dae76d0f0cee6df0d17c996da177c9e08703abfdb08db212fda48a5bf2
~$ docker exec -it message sh
/usr/src/app # tail -f ./text.log
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
2023-12-03 17:22:47 +0000 UTC
```

## 1.7: IMAGE FOR SCRIPT 

```shell

```

## 1.7:

```shell
```
