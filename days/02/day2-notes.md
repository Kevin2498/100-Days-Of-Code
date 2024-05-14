# Day - 02

## Learning about Containers
Learning about containers from https://www.youtube.com/watch?v=rr9cI4u1_88.

### Notes
- Virtual Machine is very heavy, it is running an OS on top of an OS.
- Docker run application on top of the system, it doesn't include the entire kernel. Docker comprises of application with enough of configurations and enough of OS layer that can bare minimum run it. It uses and interacts with the host kernel whenever required.
- Spinning up a docker container is much faster than spinning up a VM.
- Whenever we spin a docker container a docker virtual volume is also created for each containers.
- To remove all containers (stopped) we could run the command ```docker container prune```.
- To list docker volume run the command ```docker volume ls```.


### Extra Notes
- View a summary of image vulnerabilities and recommendations → ```docker scout quickview mongo```.
- View vulnerabilities → ```docker scout cves mongo```.
- View base image update recommendations → ```docker scout recommendations mongo```.
- Include policy results in your quickview by supplying an organization → ```docker scout quickview mongo --org <organization>```.