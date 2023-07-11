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

flask db init       to initialize the database
flask db migrate    to migrate new changes
flask db upgrade    to upgrade and so on.

# Issues
Migrate not working for version issue on Flask

https://medium.com/nerd-for-tech/developing-a-simple-create-read-update-and-delete-crud-application-using-flask-and-mariadb-f037a5798ee2

https://medium.com/thedevproject/use-flask-cli-to-create-commands-for-your-postgresql-on-heroku-in-6-simple-steps-e8166c024c8d


