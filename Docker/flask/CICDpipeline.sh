#!/usr/bin/env bash
set -e

mkdir ./app
cd app
#CI pull из github - проверка pylint - создания артифакта - push в docker hub
git clone git@github.com:vkv0220/lectures-cloud.git
cd ./lectures-cloud/Docker/flask/
pylint hello.py --errors-only
if [[ $? > 0 ]]; then
  echo 'pylint checked file and found an error'
  echo "pipeline couldn't be finished"
  exit 5
fi
docker build -t vkv0220/flask:2.0 .
docker push vkv0220/flask:2.0

#Использовать version из git
#Version прикреплен к master
Version=$(git rev-parse --abbrev-ref HEAD)

#CD развертывание docker-compose.yaml c  image из dockerhub.
docker-compose up -d --build
