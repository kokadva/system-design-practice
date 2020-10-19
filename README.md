# System-Design-Practice

## Project Description:
I've decided to learn some system design priciples, patterns and actually build some stuff and put it here. 

#### You'll need docker and docker-compose installed for every project here

### Project 0: Simple load balancing of a stateless server app

#### Description:
Couple of a simple python/flask app instances with an nginx as a load balancer in front, everything run in docker containers

#### Technologies used:
* Python/Flask
* Nginx
* Docker/Docker-Compose

#### How to run:
1. Build `flask-app` image by going to the `flask-app` folder and running: `docker build -t flask-app .`
2. Build `nginx-app` image by going to the `nginx-app` folder and running: `docker build -t nginx-app .`
3. Run two instances of `flask-app` and a nginx load balancer (`nginx-app`) by running: `docker-compose up`
