# Containerization for Sentiment Analysis API

## Table of Content
- [Description](#description) 
- [Environment requirements](#environment-requirement)
- [Installation](#installation)
- [How To Use](#how-to-use)
- [Implementation](#implementation)
- [API Monitoring](#api-monitoring)

 ---

### Description 
 ![RESTFULL APIS with Docker Base](https://miro.medium.com/max/1400/1*FcigeCUocGksT_eaQ4JH9w.png)

 Simple Scikit-Learn model deployed as a REST API using Flask RESTful.
 Sentiment prediction : [Naives Bayes classifier](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)

### Environment Requirement

 This Modul depends on : 

- Flask
- uWSGI
- Chalice
- Matplotlib
- scikit-learn
- Numpy
- Pandas
- Flask_restful
- scipy

This Module is [Docker](https://docs.docker.com/) Containerized, All dependencies will be installed while deploying the conatiner.

### Installation

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) downloaded and installed.
1. Clone the [dockerizeSentApi](https://github.com/ahmed-mahmoud-allmyhomes/dockerizeSentApi) Repository.

### How to use

1. cd to the Downloaded Repository.
2. .

```sh
docker-compose up -d --build
```

3. test if deployment completed 

```sh
 curl http://127.0.0.1:5000/
 or
  curl http://localhost:5000/
```

4. run Sentiment Pridector API command

```sh
curl -X GET http://127.0.0.1:5000/statment -d query='$query'

{"prediction": "Positive/Negative", "confidence": int}
```
### Implementation

- for Implementation testing in case you don't have all the required dependencies

```sh
$ docker ps
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS  

copy flask container_ID 

docker exec -it container_ID /bin/(bash or zsh)
output:
root@container_ID:/app# python3
>>> Implement 
```
### API Monitoring 

#### why Monitoring ?

- Performance over time
- Largest API users
- Most commonly used API features
- Error occurrence in the API

* Potintial is Kibana 
![kibana](https://linagora.com/wp-content/uploads/2018/06/Kibana-logo-2.png)
