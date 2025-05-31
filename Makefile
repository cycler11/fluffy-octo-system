.PHONY: install test run docker-build docker-run migrate lint format

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PYTHON) setup.py develop

test:
	$(PYTHON) -m pytest tests/ -v --cov=app --cov-report=html

run:
	$(PYTHON) -m flask run

docker-build:
	docker build -t library-app .

docker-run:
	docker run -p 5000:5000 library-app

migrate:
	$(PYTHON) -m flask db init
	$(PYTHON) -m flask create-migration "Initial migration"
	$(PYTHON) -m flask db upgrade
	$(PYTHON) -m flask init-db

lint:
	$(PYTHON) -m flake8 app tests
	$(PYTHON) -m black --check app tests

format:
	$(PYTHON) -m black app tests
