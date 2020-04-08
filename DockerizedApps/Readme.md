Resources :
https://docs.docker.com/docker-for-mac/
https://docs.docker.com/compose/gettingstarted/
https://medium.com/travis-on-docker/how-to-dockerize-your-go-golang-app-542af15c27a2

# Important INFO :
1. Once the frontend/Webapp is comlpetely dockerized
2. Need to check with Django/CompareDjango/CropFaces/LiveStreamingOutput/PeopleAnomalyDetection
3. Need to make sure that the dockerized application still functions the way it is supposed with
all the integrations done
4. Verify all features worked on are avaiable in the final version 
# To run from docker  :
**To build**
1. docker build -t anirudhrv1234/goapi .

**To run GO API (ERROR : connect to mongodb)**
1. To build: docker build -t anirudhrv1234/goapi .

2. Remote: docker run --rm -it -p 8080:8080 anirudhrv1234/goapi

3. Local: docker run --rm -p 8080:8080 anirudhrv1234/goapi

**To run NodeServer (Node JS)**

1. Local: docker run -p 4000:4000 anirudhrv1234/nodeserver

**To run Client (React JS)**


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
