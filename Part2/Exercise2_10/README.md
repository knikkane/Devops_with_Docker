To ensure that Docker Compose is not exposing the directly accessible ports in the host network we just simply remove them from [docker-compose.yml](docker-compose.yml)

```shell
~$ docker run -it --rm --network host networkstatic/nmap localhost
Starting Nmap 7.92 ( https://nmap.org ) at 2024-01-04 09:30 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000020s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
631/tcp open  ipp

```
