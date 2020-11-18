PIP_CMD ?= pip
VENV_DIR ?= .venv
VENV_RUN = . $(VENV_DIR)/bin/activate

usage:           ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install:         ## Install dependencies
	(test `which virtualenv` || $(PIP_CMD) install --user virtualenv) && \
		(test -e $(VENV_DIR) || virtualenv $(VENV_OPTS) $(VENV_DIR)) && \
		($(VENV_RUN); $(PIP_CMD) -q install -r requirements.txt)

publish:         ## Publish the library to the central PyPi repository
	($(VENV_RUN) && ./setup.py sdist upload)

.PHONY: usage install publish
