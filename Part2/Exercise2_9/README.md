# Changes
With nginx as proxy the REACT_APP_BACKEND_URL was modified from http://localhost:8080 to http://localhost/api to align with the proxy config. 
Similarly the backend environment variable REQUEST_ORIGIN was updated from http://localhost:5000 to http://localhost

# Docker files
[docker-compose.yml](docker-compose.yml)

[Frontend](Frontend/Dockerfile)

[Backend](Backend/Dockerfile)

```shell
~$ mkdir database
~$ docker compose up
```
<img src=Screenshot_devops_with_dock_p02_e29.png width="60%">
