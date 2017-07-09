SHELL=/bin/bash

.PHONY: static

SCRIPT = scripts/manage.py
PIP = venv/bin/pip

clean:
	rm -rf var

env:
	virtualenv -p python venv
	$(PIP) install --upgrade pip setuptools
	$(PIP) install --upgrade -r requirements.txt
	$(PIP) install -e .
	mkdir -p var

server:
	$(SCRIPT) runserver 0.0.0.0:8000

db:
	$(SCRIPT) makemigrations
	$(SCRIPT) migrate

tests:
	$(SCRIPT) test

clean_bytescode:
	find -name "*.pyc" -not -path "./venv/*" | xargs rm

static:
	$(SCRIPT) collectstatic

cleanenv: clean env

