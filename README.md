# Movie-List
Sennder movie list -- Studio Ghibli API

## To run the app on docker:
- Clone the repo to your local
- cd into folder.
- Run the following command `docker-compose up --build -d`
- To check the status of the running containers, run the following command `docker ps -a`
- To get inside the "web" docker container using this: `docker exec -u 0 -it Container_ID bash`

### To restart the server:
- Run the server like that: `./manage.py runserver` or restart the "web" container.

### To run tests:
`./manage.py test`

### Application using: 
- Django: 3.1.2
- requests: 2.25.0
- python-memcached: 1.59  ---> under development & testing.
