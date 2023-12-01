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

## 1.3: 
