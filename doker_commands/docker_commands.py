'''

to check the docker version : docker --version

to check the docker images : docker images

to pull the images ubuntu : docker pull ubuntu

to check the running  containers in docker : docker ps

to check the available and running containers in docker : docker ps -a

to run the docker container image : docker run -it -d 'image name'
-it : interactive mode
-d : run in deamon thread mode


to restart the container : docker restart 'container id'

to stop the container: docker stop 'container id'

to remove the container : docker rm 'container id'

unless the container is stopped , it cant be removed

to remove the image from docker : docker rmi 'image id'

to kill the running container : docker kill 'container id'

to check the details of a container : docker inspect 'container id'

to find the docker logs command is : docker logs 'container id'













'''