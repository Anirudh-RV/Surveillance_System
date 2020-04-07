Resources :
https://docs.docker.com/docker-for-mac/
https://docs.docker.com/compose/gettingstarted/
https://medium.com/travis-on-docker/how-to-dockerize-your-go-golang-app-542af15c27a2

# To run from docker  :
**To build**
1. docker build -t anirudhrv1234/goapi .

**To run mongo locally**
1.

**To run GO API (ERROR : connect to mongodb)**
1. Remote: docker run --rm -it -p 8080:8080 anirudhrv1234/goapi

2. Local: docker run --rm -p 8080:8080 anirudhrv1234/goapi

**To run NodeServer (Node JS)**

1. Local: docker run -p 4000:4000 anirudhrv1234/nodeserver

**To run Client (React JS) integrate completely before dockerizing**


#Commands to run a Docker app (GENERAL):

**To make directory :**
1. mkdir test
2. cd test

**To make the app :**
1. touch myapp.py
2. open myapp.py
3. -Copy & Paste the required code

**To define the requirements/dependencies :**
1. touch requirements.txt
2. open requirements.txt
3. -Copy & Paste the required dependencies

**To create Dockerfile**
1. touch Dockerfile
2. open Dockerfile
3. -Copy & Paste the system configuration

**To create docker-compose.yml**
1. touch docker-compose.yml
2. open docker-compose.yml
3. -Copy & Paste the required configuration

**Run the App**
1. docker-compose up

**To delete images**
1. docker system prune
