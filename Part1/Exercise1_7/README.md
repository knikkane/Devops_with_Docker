## 1.7:  IMAGE FOR SCRIPT
After you have filled the Dockerfile, build the image with the name "curler"

```shell
~$ chmod +x website.sh
~$ docker build . -t curler
[+] Building 48.6s (6/6) FINISHED                                                                                                                                                                               docker:default
 => [internal] load .dockerignore                                                                                                                                                                                         0.0s
 => => transferring context: 2B                                                                                                                                                                                           0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                                      0.0s
 => => transferring dockerfile: 251B                                                                                                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/ubuntu:20.04                                                                                                                                                           2.3s
 => [1/2] FROM docker.io/library/ubuntu:20.04@sha256:f5c3e53367f142fab0b49908550bdcdc4fb619d2f61ec1dfa60d26e0d59ac9e7                                                                                                    12.4s
 => => resolve docker.io/library/ubuntu:20.04@sha256:f5c3e53367f142fab0b49908550bdcdc4fb619d2f61ec1dfa60d26e0d59ac9e7                                                                                                     0.0s
 => => sha256:fe8a36445d3d850960d6a24554f2cf4e19d82ba1e611e3e8713bd7b76989623d 424B / 424B                                                                                                                                0.0s
 => => sha256:83a4bf3bb050e11e0f3bfdcfaff38eeb1dd851b7a362d930cd590dd97b3b1687 2.30kB / 2.30kB                                                                                                                            0.0s
 => => sha256:25ad149ed3cff49ddb57ceb4418377f63c897198de1f9de7a24506397822de3e 27.51MB / 27.51MB                                                                                                                          9.8s
 => => sha256:f5c3e53367f142fab0b49908550bdcdc4fb619d2f61ec1dfa60d26e0d59ac9e7 1.13kB / 1.13kB                                                                                                                            0.0s
 => => extracting sha256:25ad149ed3cff49ddb57ceb4418377f63c897198de1f9de7a24506397822de3e                                                                                                                                 2.4s
 => [2/2] RUN apt update; apt install -y curl                                                                                                                                                                            32.7s
 => exporting to image                                                                                                                                                                                                    1.1s 
 => => exporting layers                                                                                                                                                                                                   1.1s 
 => => writing image sha256:64662040eba1e77bb5969e9f61f3031d933d700875cd4df2ca5f806c1726bc36                                                                                                                              0.0s 
 => => naming to docker.io/library/curler                                                                                                                                                                                 0.0s 
```

Execute
```shell
~$ docker run -it curler                                                                                                                  
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
