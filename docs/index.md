# Sentiment Analyzer Microservice

A FastAPI-based microservice for sentiment analysis following the 12-Factor App methodology.

## Overview

The Sentiment Analyzer is a simple microservice that analyzes the sentiment of text inputs and categorizes them as positive, negative, or neutral using a rule-based approach.

## Features

- **Sentiment Analysis API**: Simple REST endpoint for text sentiment analysis
- **Rule-based Algorithm**: Uses word lists to determine sentiment without external dependencies
- **12-Factor App Design**: Follows best practices for cloud-native applications
- **Containerized**: Ready for deployment in any container environment

## Architecture

The application follows a clean, modular architecture:

```
app/
├── api/            # API endpoints and routers
├── core/           # Core configuration and settings
├── models/         # Data models and schemas
└── services/       # Business logic services
```

### 12-Factor App Principles

This project implements the [12-Factor App](https://12factor.net/) methodology:

1. **Codebase**: Single codebase tracked in version control
2. **Dependencies**: Explicitly declared and isolated
3. **Config**: Stored in environment variables
4. **Backing Services**: Treated as attached resources
5. **Build, Release, Run**: Strict separation of build and run stages
6. **Processes**: Stateless and share-nothing
7. **Port Binding**: Self-contained service
8. **Concurrency**: Scale out via process model
9. **Disposability**: Fast startup and graceful shutdown
10. **Dev/Prod Parity**: Development environment similar to production
11. **Logs**: Treated as event streams
12. **Admin Processes**: Run as one-off processes

## Getting Started

Please refer to the [README.md](https://github.com/shreyaupretyy/sentiment-analyzer) for installation and usage instructions.
