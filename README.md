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
