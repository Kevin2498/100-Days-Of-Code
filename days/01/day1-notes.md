# Day - 01

## Learning about Containers
Learning about containers from https://www.youtube.com/watch?v=rr9cI4u1_88.

### Notes
- Images in docker is something like CD/DVD using which we want to run something. For example we used to use Ubuntu from a physical disk.
- Container is the place where we run our images.
- How to pull a docker image from public repository is using ``docker pull`` command.
```
docker pull postgres
```
- To list image which are present in the system use:
```
docker image ls
```
- ```docker ps``` is used to list containers (running, stopped or etc).
- To run an image or install and image on container and use it, we run the below command.
```
docker run
```
- Whenever we run a new image on container, the container name changes everytime.
- Sometime to spin a container of an image, we need to provide some parameters in enviornment variables.
- To run a docker container of a postgres image we could use the below command:
```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres:tag
```
- To stop a docker container we could run the below comand:
```
docker stop [CONTAINER NAME/CONTAINER ID]
--------
docker container stop [CONTAINER NAME/CONTAINER ID]
```
Note: If we specify the first four characters of the container id which is unique across all the running containers then it would stop the respective container.
- If we don't want to use the latest image version and if we want to use any old image version then we could specify the same like below:
```
docker run --name postgres-old -e POSTGRES_PASSWORD=mysecretpassword -d postgres:13.5
```
- docker run command will first search for image locally if it is not able to find then it'll search on the internet and pull the image based on the tag which we have specified.
- Use the command ```docker container ls -a``` to list the containers which are running or stopped.
