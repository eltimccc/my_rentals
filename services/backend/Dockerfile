FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

RUN pip install alembic

COPY src/ .
CMD ["bash"]