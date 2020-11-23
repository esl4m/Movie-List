# Movie-List
Sennder movie list -- Studio Ghibli API

## To run the app on docker:
- Clone the repo to your local
- cd into folder.
- Run the following command: `docker-compose up --build -d` (this will build the docker services and run it in background)
- To check the status of the running containers, run the following command `docker ps -a`
- To get inside the "movies_app" docker container: `docker exec -u 0 -it Container_ID bash`

### To restart the server:
- Run the server: `./manage.py runserver` or restart the "movies_app" container `docker restart Container_ID`

### To run tests:
`./manage.py test`

### Application using: 
- Django: 3.1.2
- requests: 2.25.0
- python-memcached: 1.59  ---> under development & testing.
