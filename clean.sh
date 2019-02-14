#!/bin/bash

# to clean all pycache
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs sudo rm -rf

# to clean db and related media:
sudo rm -rf db src/media

# to clean .pytest_cache
sudo rm -rf src/.pytest_cache

# to clean .env and .coverage
[ -f src/.coverage ] && sudo rm src/.coverage
[ -f src/core/.env ] && sudo rm src/core/.env
