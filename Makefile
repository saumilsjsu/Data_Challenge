run-docker: docker-build docker-up

docker-build:
	docker-compose build

docker-up:
	docker-compose up

# command to run the python script from within the running docker container
# docker exec -it $(docker ps | grep sfl_scientific_mysql | awk '{print $1}') python3 etl1.py