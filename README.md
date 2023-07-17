# flask_microservice

Flask API connected with Django 'microservice_python'

# flask_installation

sudo apt install python3-flask

# Docker compose commands

docker-compose up --build (permission issue use 'sudo')

docker image prune -a (Removing all unused images)

# Bug Fixes

## db container not stop or down

sudo aa-remove-unknown ( not nessasary to remove all unknown author files and programs)

docker container kill $(docker ps -q)

docker-compose down

docker-compose exec backend sh

# Install Postman to check API (not needed in production server)

sudo snap install postman


# Migrate Database

First go into the backend server: docker-compose exec backend sh

python manager.py db init       #to initialize the database
python manager.py db migrate    #to migrate new changes to db
python manager.py db upgrade     to upgrade and so on.

# RabbitMQ configuration and installation (CloudAMPQ)

Log in to CloudAMPQ
Create a team and create a (free tier) instance in it
Go into the instance
Copy the AMPQ URI (like amqps://sxhupzyl:***@armadillo.rmq.cloudamqp.com/sxhupzyl) 

My URL:
amqps://sxhupzyl:6qwtiY5A6CJKv3PTVQY651zRzHAb5nib@armadillo.rmq.cloudamqp.com/sxhupzyl

#Environment Variable
