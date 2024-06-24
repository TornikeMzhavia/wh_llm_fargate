# Deploing FastAPI on AWS ECS with Fargate and a load balancer

This installs FastAPI in a Docker container and runs it on ECS Fargate with an Application Load Balancer at the front.

## Requirements
- AWS CDK
- [CDK Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).
- docker and docker-compose to run locally

## To run locally

`docker-compose` is used to run locally.

### Start the API locally

```bash
$ docker-compose up
```

### Call  local API
```bash
$ curl http://127.0.0.1:5555

{"message":"FastAPI running in a Docker container"}
```

## Deploy

The [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) is used to deploy the application.

### Deploy

```bash
$ cd cdk
$ cdk deploy
```

### How to call the API
```bash
$ curl http://XXXX.eu-west-1.elb.amazonaws.com

{"message":"FastAPI running in a Docker container"}
```
