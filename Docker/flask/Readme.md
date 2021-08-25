Simple CI/CD project on github. You can use part of the project for your own purposes

1. hello.py - flask app, works with postgres database, shows current temp in Tomsk)
2. Dockerfile - to build docker container with requirements. To run your own container with flask app
you can run you own container via cmd from dockerhub:
docker run -d -e API_KEY=InsertYouApiKeyHere -e NAME="InsertYouNameHere" -p 5000:5000 vkv0220/flask:latest
ApiKey you can find at http://api.openweathermap.org/
3. docker-compose.yml - to build all the project including postgres db and app
4. CICDpipeline.sh - downloads the project, checks hello.py by pylint, if there are no errors, pushes builded app to dockerhub and runs the project on the local environment.

* NOTE: don't forget about environmet variables.
You can add your API_KEY and NAME by the commands:
export NAME=YouName
export API_KEY=LongAPIKey
