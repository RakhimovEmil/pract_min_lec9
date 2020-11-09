build:
	docker-compose build

up: build
	docker-compose up

stop:
	docker-compose stop

healthcheck:
	@which docker || echo "docker is not installed"
	@which docker-compose || echo "d-c is not installed"

.PHONY: build up stop healthcheck
