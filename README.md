# Clone inside a folder named django:
Why it is needed. Because Docker-compose creates service names like: "parent.folder.name"_"service.name" 
So django service will be named "django"
and will use "http://django:8000" in other container code

# flask_microservice

Flask API connected with Django 'microservice_python'

# flask_installation

sudo apt install python3-flask

# Create the Docker network:
Before running the containers, we need to create the external network (my_network) that will be shared by both the "admin" and "main" folders.

docker network create my_shared_network

# first run django app then flask app 

# Docker compose commands

docker-compose up --build (permission issue use 'sudo')

docker-compose down

docker image prune -a (Removing all unused images)


# Migrate Database

First go into the backend server: docker-compose exec backend sh

python manager.py db init       #to initialize the database
python manager.py db migrate    #to migrate new changes to db
python manager.py db upgrade     to upgrade and so on.


# Bug Fixes

## db container not stop or down

sudo aa-remove-unknown ( not nessasary to remove all unknown author files and programs)

docker container kill $(docker ps -q)

docker-compose down

docker-compose exec backend sh

# Install Postman to check API (not needed in production server)

sudo snap install postman

# RabbitMQ configuration and installation (CloudAMPQ)

Log in to CloudAMPQ
Create a team and create a (free tier) instance in it
Go into the instance
Copy the AMPQ URI (like amqps://sxhupzyl:***@armadillo.rmq.cloudamqp.com/sxhupzyl) 

My URL:
amqps://sxhupzyl:6qwtiY5A6CJKv3PTVQY651zRzHAb5nib@armadillo.rmq.cloudamqp.com/sxhupzyl
