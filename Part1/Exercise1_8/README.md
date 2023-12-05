Docker build

```shell
~$ docker build . -t web-server
[+] Building 2.7s (6/6) FINISHED                                                                                                                                                                                docker:default
 => [internal] load .dockerignore                                                                                                                                                                                         0.0s
 => => transferring context: 2B                                                                                                                                                                                           0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                                      0.0s
 => => transferring dockerfile: 156B                                                                                                                                                                                      0.0s
 => [internal] load metadata for docker.io/devopsdockeruh/simple-web-service:alpine                                                                                                                                       2.7s
 => [1/2] FROM docker.io/devopsdockeruh/simple-web-service:alpine@sha256:dd4d367476f86b7d7579d3379fe446ae5dfce25480903fb0966fc2e5257e0543                                                                                 0.0s
 => => resolve docker.io/devopsdockeruh/simple-web-service:alpine@sha256:dd4d367476f86b7d7579d3379fe446ae5dfce25480903fb0966fc2e5257e0543                                                                                 0.0s
 => CACHED [2/2] RUN ./server&                                                                                                                                                                                            0.0s
 => exporting to image                                                                                                                                                                                                    0.0s
 => => exporting layers                                                                                                                                                                                                   0.0s
 => => writing image sha256:6583a504df03d3994e61d5912500d421cdc12edba9636b8641cbc3085dc32e50                                                                                                                              0.0s
 => => naming to docker.io/library/web-server                                                                                                                                                                             0.0s
```

Running the built "web-server" image

```shell
~$ docker run web-server
[GIN-debug] [WARNING] Creating an Engine instance with the Logger and Recovery middleware already attached.

[GIN-debug] [WARNING] Running in "debug" mode. Switch to "release" mode in production.
 - using env:	export GIN_MODE=release
 - using code:	gin.SetMode(gin.ReleaseMode)

[GIN-debug] GET    /*path                    --> server.Start.func1 (3 handlers)
[GIN-debug] Listening and serving HTTP on :8080

```
