to run all: docker-compose up (-d for detached mode)
to get into django container bash: docker-compose exec django bash
to run all tests: pytest -v --cov . --cov-report term-missing --cov-fail-under=100 --flake8 -n 8
