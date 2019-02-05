# docker-compose up -d
# docker-compose exec django bash
# pytest -v --cov . --cov-report term-missing --cov-fail-under=100 --flake8 -n 8

to clean pycache: find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs sudo rm -rf
