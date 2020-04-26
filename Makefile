CONTAINER_NAME=phone-book
PROJECT_NAME=droppt-83468

build:
ifndef TAG
	$(error TAG is undefined)
endif
	docker build -f Dockerfile  -t $(CONTAINER_NAME) .
	docker tag $(CONTAINER_NAME) gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):stg_$(TAG)
	docker tag $(CONTAINER_NAME) gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):stg_latest

push: build
	# push the built image to the gcloud container registry
	docker push gcr.io/$(PROJECT_NAME)/$(CONTAINER_NAME):stg_$(TAG)
