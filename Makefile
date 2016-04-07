PYTHON := python
VENV := env-$(PYTHON)

# for travis

$(VENV)/bin/python:
	[ -d $(VENV) ] || $(PYTHON) -m virtualenv $(VENV) || virtualenv $(VENV)
	$(VENV)/bin/pip --quiet install --upgrade setuptools pip
	$(VENV)/bin/python setup.py develop


.PHONY: dev-env
dev-env: $(VENV)/bin/python


# for testing
.PHONY: test
test: dev-env
	$(VENV)/bin/pip --quiet install --upgrade funcsigs mock
	$(VENV)/bin/python -m unittest discover -v -s tests


.PHONY: clean
clean:
	rm -rf env-python/ dist/ docs/
	find . -name "*.pyc" -type f -delete


# for document
.PHONY: docs
docs: dev-env clean
	$(VENV)/bin/pip --quiet install --upgrade epydoc
	rm -rf docs/
	$(VENV)/bin/epydoc -o docs --html -v jetpackid
