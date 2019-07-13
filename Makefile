WORKDIR = /vagrant
SHELL = /bin/bash
PSQL = sudo -u postgres psql
DBNAME = flask_api

db/console:
	$(PSQL) $(DBNAME)

db/create:
	@echo "--> create DB"
	$(PSQL) -c "DROP DATABASE IF EXISTS $(DBNAME);"
	$(PSQL) -c "CREATE DATABASE $(DBNAME);"

pip/freeze:
	@echo "--> saving python dependencies to requirements.txt"
	pip freeze > requirements.txt

pip/update:
	@echo "--> updating python dependencies from requirements.txt"
	cd $(WORKDIR)/backend && \
		sudo pip install -r requirements.txt && \
		cd $(WORKDIR)

npm/update:
	@echo "--> updating node dependencies from package.json"
	cd $(WORKDIR)/frontend && npm install && cd $(WORKDIR)

npm/build:
	@echo "--> build/transpile javascript to a /dist directory for flask to serve files"
	cd $(WORKDIR)/frontend && npm run build && cd $(WORKDIR)

venv/setup: venv/setup_venv venv/setup_shell

venv/setup_shell:
	@echo "--> configuring python environment"
	(test -f ~/.bash_profile  && grep venv/bin/activate ~/.bash_profile) || \
		echo "cd $(WORKDIR) && source venv/bin/activate" >> ~/.bash_profile

venv/setup_venv:
	@echo "--> creating python virtual environment"
	test -d venv || python3 -m venv venv

flask/app:
	@echo "--> run the flask application"
	cd $(WORKDIR)/backend && flask run --host=0.0.0.0

test:
	@echo "--> run the tests for the project"
	docker-compose -f docker-compose.test.yml run --rm test-api coverage run -m pytest -v


test_report:
	@echo "--> run the test test_report for the project"
	docker-compose -f docker-compose.test.yml run --rm test-api coverage report

lint:
	@echo "--> run the linting for the project"
	docker-compose -f docker-compose.test.yml run --rm test-api flake8

.PHONY: all
