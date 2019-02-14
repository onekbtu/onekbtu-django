#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push muslimbeibytuly/onekbtu-django:${TRAVIS_BRANCH}
