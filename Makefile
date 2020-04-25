CONTAINER_NAME=icook-backend
PROJECT_NAME=droppt-83468

build:
ifndef TAG
	$(error TAG is undefined)
endif
	docker build -f docker/stagDockerfile  -t $(CONTAINER_NAME) .
	docker tag $(CONTAINER_NAME) gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):stg_$(TAG)
	docker tag $(CONTAINER_NAME) gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):stg_latest

push: build
	# push the built image to the gcloud container registry
	docker push gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):stg_$(TAG)


build_prod:
ifndef TAG
	$(error TAG is undefined)
endif
	docker build -f docker/prodDockerfile  -t $(CONTAINER_NAME) .
	docker tag $(CONTAINER_NAME) gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):prod_$(TAG)
	docker tag $(CONTAINER_NAME) gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):prod_latest

push_prod: build_prod
	# push the built image to the gcloud container registry
	docker push gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):prod_$(TAG)