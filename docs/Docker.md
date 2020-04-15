# Docker with Django

[Link](https://docs.docker.com/docker-for-windows/) to use Docker on Windows 10

### Install Python 3.7 in docker container

Create a Docker file in root folder with below content
 
    FROM python:3.7
    
    WORKDIR /usr/src/app
    
    COPY ./requirements.txt /usr/src/app

```FROM``` => Docker image pulled from DockerHub (or cached locally)
```WORKDIR``` => Source folder inside container
```COPY``` => Copy from local folder to source folder inside container

### Build docker image
 
    docker build -t phone_book .
    
    Sending build context to Docker daemon  2.521MB
    Step 1/3 : FROM python:3.7
     ---> 859d8ec7db6a
    Step 2/3 : WORKDIR /usr/src/app
     ---> Running in 67ae97a6f92e
    Removing intermediate container 67ae97a6f92e
     ---> 7a59173bc14d
    Step 3/3 : COPY ./requirements.txt /usr/src/app
     ---> 05327091cd47
    Successfully built 05327091cd47
    Successfully tagged phone_book:latest
 
```-t``` => Tag for our docker image

```.```  => Look for a Dockerfile in current folder

### Run docker image

    docker run -it phone_book
    
    Python 3.7.7 (default, Mar 31 2020, 15:46:29)
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import platform
    >>> platform.platform()
    'Linux-4.19.76-linuxkit-x86_64-with-debian-10.3'
    >>>
 
    docker run -it phone_book ls
    requirements.txt

### Access contents inside docker container (SSH to container)
 
    docker run -it phone_book bash
    root@c40dfe9bb74b:/usr/src/app#
    
    root@c40dfe9bb74b:/usr/src/app# cat requirements.txt
    asgiref==3.2.3
    Django>=3.0.3
    ........
 
### Exit the shell (which also stops the container):

    root@c40dfe9bb74b:/usr/src/app# exit
    exit
    
    (env) C:\Sushma\Github\PhoneBook>

### Using docker-compose 
Services used by our project are defined in it. To build it, run below command -

    docker-compose up
    
Everytime you modify the source files, you should rebuild the container. 
To (re)build and start the container using a single command, run -
    
    docker-compose up --build
    
    Creating network "phonebook_default" with the default driver
    Building mypython
    Step 1/3 : FROM python:3.7
    3.7: Pulling from library/python
    ......
    Successfully built 20990a0e0495
    Successfully tagged phonebook_mypython:latest
    WARNING: Image for service mypython was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
    Creating phonebook_mypython_1 ... done                                                                                                      Attaching to phonebook_mypython_1
    mypython_1  | requirements.txt
    phonebook_mypython_1 exited with code 0

It will build Dockerfile from path defined in docker-compose file.

### List all images

 > docker image ls
 
### Remove one or more specific images
Use the docker images command with the -a flag to locate the ID of the images you want to remove. This will show you every image, including intermediate image layers. When you’ve located the images you want to delete, you can pass their ID or tag to docker rmi:

List:

    docker images -a

Remove:

    docker rmi Image Image


### List all containers

 > docker container ls --all

List only your running containers:

 > docker container ls
 
### Remove one or more specific containers

Use the docker ps command with the -a flag to locate the name or ID of the containers you want to remove:

List:

    docker ps -a

Remove:

    docker rm ID_or_Name ID_or_Name

### Pull and run a Dockerized nginx web server (we name it, webserver):

 > docker run --detach --publish 80:80 --name webserver nginx
 
    TODO: FIX THIS ERROR. This is most probably due to the firewall
    846f7d6f7ee759e3688a871ad80ded2f2a0e6beccc103bb4a4a46733dac943a7
    docker: Error response from daemon: Ports are not available: listen tcp 0.0.0.0:80: 
    bind: An attempt was made to access a socket in a way forbidden by its access permissions.
 
This is not working yet!

    When it is fixed, point your web browser at http://localhost to display the nginx start page. 
    (You don’t need to append :80 because you specified the default HTTP port in the docker command.)

### Stop the running nginx container by the name we assigned it, webserver:

 >  docker container stop webserver

### 

Remove all three containers by their names (the name given during container creation):

 > docker container rm webserver nginx hello-world webserver_docker

### Deleting / Purging All Unused or Dangling Images, Containers, Volumes, and Networks

Docker provides a single command that will clean up any resources — images, containers, volumes, and networks — that are dangling (not associated with a container):

    docker system prune
 
    WARNING! This will remove:
      - all stopped containers
      - all networks not used by at least one container
      - all dangling images
      - all dangling build cache
    
    Are you sure you want to continue? [y/N] y
    Deleted Containers:
    846f7d6f7ee759e3688a871ad80ded2f2a0e6beccc103bb4a4a46733dac943a7
    ..........

    Deleted Images:
    deleted: sha256:655034c37c701b39dc8e36ceff157d7b04fed48a582e33b441bdcea9b0c2bac4
    deleted: sha256:1013c34ab5df6fbcd4ba7f295689734bf10057197bd0a81af2b6680936e01f84
    ...........
    Total reclaimed space: 424.4MB

To additionally remove any stopped containers and all unused images (not just dangling images), add the -a flag to the command:

    docker system prune -a
    
    ............
    Total reclaimed space: 3.471GB
