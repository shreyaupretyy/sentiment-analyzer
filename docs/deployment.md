# Deployment Guide

This document outlines how to deploy the Sentiment Analyzer service to various environments.

## Docker Deployment

### Local Docker Deployment

1. Build and run the application:

```bash
docker-compose up --build
```

2. Access the API at `http://localhost:8000`

### Cloud Deployment

#### Azure Container Instances

1. Build and push the Docker image:

```bash
az acr build --registry <your-registry> --image sentiment-analyzer:latest .
```

2. Deploy to Azure Container Instances:

```bash
az container create \
  --resource-group <your-resource-group> \
  --name sentiment-analyzer \
  --image <your-registry>.azurecr.io/sentiment-analyzer:latest \
  --dns-name-label sentiment-analyzer \
  --ports 8000
```

#### AWS ECS

1. Create an ECS task definition (example):

```json
{
  "family": "sentiment-analyzer",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::your-account-id:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "sentiment-analyzer",
      "image": "your-repo/sentiment-analyzer:latest",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 8000,
          "hostPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "ENVIRONMENT",
          "value": "production"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/sentiment-analyzer",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512"
}
```

2. Create an ECS service to run the task definition

## Kubernetes Deployment

1. Create a Kubernetes deployment manifest:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sentiment-analyzer
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sentiment-analyzer
  template:
    metadata:
      labels:
        app: sentiment-analyzer
    spec:
      containers:
      - name: sentiment-analyzer
        image: your-repo/sentiment-analyzer:latest
        ports:
        - containerPort: 8000
        env:
        - name: ENVIRONMENT
          value: "production"
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 15
          periodSeconds: 20
```

2. Create a Kubernetes service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sentiment-analyzer
spec:
  selector:
    app: sentiment-analyzer
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
```

3. Apply the manifests:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Environment Variables

Make sure to set these environment variables in your deployment environment:

| Variable      | Production Value        |
|---------------|-----------------------|
| APP_NAME      | sentiment-analyzer    |
| APP_VERSION   | 0.1.0                |
| ENVIRONMENT   | production           |
| HOST          | 0.0.0.0              |
| PORT          | 8000                 |
| LOG_LEVEL     | info                 |

## Monitoring

The service exposes a `/health` endpoint that can be used for health checks by monitoring systems.