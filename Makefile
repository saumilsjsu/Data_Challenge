run-docker: docker-build docker-up

docker-build:
	docker-compose build mysql

docker-up:
	docker-compose up mysql

# command to run the python script from within the running docker container
# docker exec -it $(docker ps | grep sfl_scientific_mysql | awk '{print $1}') python3 etl1.py

build-tensorflow:
	docker-compose build tensorflow

run-tensorflow:
	docker-compose run tensorflow /bin/bash

tensorflow: build-tensorflow run-tensorflow

serve-tensorflow:
	docker-compose up tensorflow-serving

test-model:
	python src/test_model.py

test-tensorflow-server:
	pip install -r requirements.txt
	python src/tf_serving_predict.py