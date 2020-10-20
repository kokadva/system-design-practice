# System-Design-Practice

## Project Description:
I've decided to learn some system design principles, patterns and actually build some stuff and put it here. 

#### You'll need docker and docker-compose installed for every project here

### Project 0: Simple load balancing of a stateless server app

#### Description:
Couple of a simple python/flask app instances with an nginx as a load balancer in front, everything runs in docker 
containers. Here `nginx` operates as a load balancer and is using `Round Robin` principle, to change that you have 
to change it's configuration file (`./nginx/nginx.conf`) according to this link 
http://nginx.org/en/docs/http/load_balancing.html


#### Technologies used:
* Python/Flask
* Nginx
* Docker/Docker-Compose

#### How to run:
Run command: `docker-compose up`

### Project 1: Asynchronism with message broker 

#### Description:
Simple server with one endpoint receiving commands for asynchronous execution which puts messages to the Rabbit MQ, and 
a worker app which is listening to the Rabbit MQ and executes command once it's received. This examples is copied from 
this source: https://medium.com/better-programming/background-processing-with-rabbitmq-python-and-flask-5ca62acf409c
// TODO add frontend app for receiving async results 

#### Technologies used:
* Python/Flask
* RabbitMQ
* Docker/Docker-Compose

#### How to run:
Run command: `docker-compose up`

