## Prerequisites

- Install Docker: https://docs.docker.com/get-docker/

## Setup

1. Clone or download this project
2. Create a `.env` file in the project root:

```
BASE_URL=https://automationexercise.com
APP_USERNAME=your_email@example.com
PASSWORD=your_password
HEADLESS=true
```

## Run Tests

```bash
docker pull your_dockerhub_username/playwright-tests:latest

docker run --rm -it \
  --env-file .env \
  your_dockerhub_username/playwright-tests:latest
```


```
