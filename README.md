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

{"message":"FastAPI LLM mockup API running in a Docker container"}
```

## Deploy

The [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) is used to deploy the application.

### Deploy

```bash
$ cd cdk
$ cdk deploy
```

AWS service names can be set by editing *cdk/config.json* file

### How to call the API
```bash
$ curl http://XXXX.eu-west-1.elb.amazonaws.com

{"message":"FastAPI LLM mockup API running in a Docker container"}
```

## Supported requests
API supports 2 types of requests
```
/question [POST]
    user_id: int
    question: str

/rate [POST]
    question_id: int
    rating: int
```

### Database
API uses SQLAlchemy and sqlite back as a sample db.
Can be replaced by AWS RDS going forward.

### Next steps
1. Propper authentication with hashing on top of the api token
2. Integrate with RDS with UUIDs rather then local sqlite
3. Add input question validation