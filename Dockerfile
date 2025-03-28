FROM python:3.13.0-slim

RUN pip install poetry
WORKDIR /UA
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .
ENTRYPOINT ["poetry", "run", "pytest", "--executor", "172.18.0.2"]

