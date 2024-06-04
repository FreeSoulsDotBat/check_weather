# Welcome to Check Weather API
Below I will leave instructions to code/use this project

## Requirements
* Project cloned on your machine;
* Docker installed;

## Instructions
1 - Set your API key from https://openweathermap.org/ to the field called 'API_KEY' inside the docker-compose.yml file.

2 - After installing docker correctly and setting your API key, you will need to run (in the root of the project) the following commands :
* `docker build -t check-weather .` (to create the image called `check-weather` according with the Dockerfile);
* `docker volume create mongodb-data` (to create a volume that will be used to our mongodb);
* `docker-compose up -d` (to lift the API, you can choose if you want or not the flag `-d`)

After all these commands, you can take a look at your http://localhost:8000/ or http://localhost:8000/docs and see the API working.
Hint: you can check the data being stored on you database with Studio 3T desktop app. (need to set the connection)

