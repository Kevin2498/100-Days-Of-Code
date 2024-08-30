## FastAPI Application deployed using Docker

### Commands used to run and set it up

1. ```docker build -t myfastapiimage .``` - Building and creating the docker image
2. ```docker run -d --name myfastapiapp -p 80:80 myfastapiimage``` - Creating and running the docker container from docker image
3. ```docker container stop myfastapiapp``` - Stopping the docker container
4. ```docker container start myfastapiapp``` - Starting the docker container
4. ```docker container prune -f``` - Pruning/Deleting the stopped docker containers.