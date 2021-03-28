# Swagger generated server

## Requirements

* Install docker (ubuntu example guide): 
  * Step-by-step [guide](https://docs.docker.com/engine/install/ubuntu/)
  * Adding your user to the docker group ```usermod -aG docker "${USER}"; newgrp docker; sudo service docker restart```

## Usage
To run the server, please execute the following from the root directory:

```
docker run -d --name mongodb --restart unless-stopped -p 27017:27017 mongo
docker run -d --name ya-back --restart unless-stopped -p 8080:8080 --net=host dimazet/ya-backend-school:latest
```

and open your browser to here:

```
http://localhost:8080/ui/
```

## Comments
- Task description in `task` directory
- Cause of docker argument `--restart unless-stopped` server restarting after VM reload 

## Links
- [DockerHub](https://hub.docker.com/repository/docker/dimazet/ya-backend-school/general)
- [GitHub](https://github.com/DimaZet/yandex-backend-school)
