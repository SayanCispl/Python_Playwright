# Must match playwright version in requirements.txt (1.51.0)
FROM mcr.microsoft.com/playwright/python:v1.51.0-noble

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BASE_URL=https://automationexercise.com
ENV HEADLESS=true

CMD ["pytest", "--alluredir=allure-results"]