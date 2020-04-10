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

# For localtunnel (Making local server port publicly avaiable):

1. brew install ruby
2. echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.bash_profile
3. gem install localtunnel
4. lt -h "http://serverless.social" -p <port number>
**Important**
1. Try using nginx for serving static folder

**Important**
1. docker stop CONTAINERID

2. lsof -P | grep ':4000' | awk '{print $2}' | xargs kill -9

3. Problem with API_Go : Until a static IP Address for the mongodb server is not found, for each system
the user has to build the API_Go container by changing the IP Address to their Computer IP in
  a. HandleUsers/UserFunc.go
  b. HandleImages/ImageFunc.go

# To run from docker  :(Build Inside respective folders)
1. 1. To build: docker build -t **-Name-** .


**Start MongoDB**
Using Mongo Atlas for cloud monogoDB
1. https://cloud.mongodb.com/v2/5e900ec2a7d1747f28c16087#metrics/replicaSet/5e900fc72e84e918f3bbb59c/explorer/GoDB/UserData/find
1. Local: docker run -d -p 27017-27019:27017-27019 --name mongodb mongo

cd74ed0cd946717155f47b95bcd85bcc8371a561a8f672c8e2506555c20d8ac4
*if error occurs saying container already running*

1. Local: docker run -d -p 27017-27019:27017-27019 --name CONTAINER ID mongo

2. Important : Make sure mongo is running on <ip-address>:27017 before running GO API

**To run GO API**
1. To build: docker build -t anirudhrv1234/goapi .

2. Remote: docker run --rm -it -p 8080:8080 anirudhrv1234/goapi

3. Local: docker run --rm -p 8080:8080 anirudhrv1234/goapi

**To run NodeServer (Node JS)**
1. To build: docker build -t anirudhrv/nodeserver .

2. Local: docker run -p 4000:4000 anirudhrv1234/nodeserver

**To run Client (React JS)**
1. To build: docker build -t anirudhrv1234/reactjs .

2. Local: docker run -p 3000:3000 anirudhrv1234/reactjs

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
