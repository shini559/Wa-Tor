.PHONY: tests

VENV_NAME?=.venv
PYTHON=${VENV_NAME}/bin/python

freeze:
	${PYTHON} -m pip freeze > requirements.txt

prepare:
	python3 -m pip install --upgrade pip
	python3 -m venv $(VENV_NAME)


install:
	pip install --no-cache-dir wheel
	${PYTHON} -m pip install -r requirements.txt

run:
	$(PYTHON) main.py


fix:
	$(PYTHON) -m black --line-length 120 ./src/*.py
	$(PYTHON) -m autopep8 --recursive --in-place --aggressive --max-line-length=120 ./src/*.py

analyse:
	$(PYTHON) -m flake8 --max-line-length=120 ./src/*.py
	$(PYTHON) -m pylint ./src
	$(PYTHON) -m pycodestyle --max-line-length=120 ./src/*.py