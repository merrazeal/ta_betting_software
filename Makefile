# BET_MAKER
bet_maker_build:
	docker compose -f ./docker/bet_maker/docker-compose.yml build

bet_maker_up:
	docker compose -f ./docker/bet_maker/docker-compose.yml up

bet_maker_down:
	docker compose -f ./docker/bet_maker/docker-compose.yml down

#LINE_PROVIDER
line_provider_build:
	docker compose -f ./docker/line_provider/docker-compose.yml build

line_provider_up:
	docker compose -f ./docker/line_provider/docker-compose.yml up

line_provider_down:
	docker compose -f ./docker/line_provider/docker-compose.yml down
