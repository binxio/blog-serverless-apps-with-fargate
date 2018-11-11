.PHONY: help create update delete
.DEFAULT_GOAL := help

environment = "example"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

create: ## create env
	@sceptre launch-env $(environment)

delete: ## delete env
	@sceptre delete-env $(environment)

docker-login:
	$(aws ecr get-login --no-include-email --region eu-west-1)

docker-build: ## build docker image
	./docker-build.sh

docker-run: ## run container
	./docker-run.sh

docker-tag: ## tag docker image
	./docker-tag.sh

docker-push: docker-build docker-tag ## push image to registry
	./docker-push.sh

get_ip: ## get the public ip
	@./get_ip.sh

run: ## run the server
	pipenv run python -m mockserver