# Docker files
[docker-compose.yml](docker-compose.yml) extended with nginx proxy
Docker files from part1

[Frontend](https://github.com/knikkane/Devops_with_Docker/blob/main/Part1/Exercise1_14/Frontend/Dockerfile)

[Backend](https://github.com/knikkane/Devops_with_Docker/blob/main/Part1/Exercise1_14/Backend/Dockerfile)

```shell
~$ docker compose up
```
```shell
~$ $ docker compose ps
NAME                    IMAGE                  COMMAND                  SERVICE             CREATED              STATUS              PORTS
p02_e28-backend-1       p02_e28-backend        "./server"               backend             About a minute ago   Up 42 seconds       0.0.0.0:8080->8080/tcp, :::8080->8080/tcp
p02_e28-db-1            postgres:13.2-alpine   "docker-entrypoint.s…"   db                  About a minute ago   Up 43 seconds       5432/tcp
p02_e28-frontend-1      p02_e28-frontend       "serve -s -l 5000 bu…"   frontend            About a minute ago   Up 43 seconds       0.0.0.0:5000->5000/tcp, :::5000->5000/tcp
p02_e28-nginx-proxy-1   nginx:1.19-alpine      "/docker-entrypoint.…"   nginx-proxy         About a minute ago   Up 43 seconds       0.0.0.0:80->80/tcp, :::80->80/tcp
p02_e28-redis-1         redis                  "docker-entrypoint.s…"   redis               About a minute ago   Up 42 seconds       6379/tcp
```
