WORKDIR = /vagrant

PSQL = sudo -u postgres psql
DBNAME = flask_api
DBUSER = vagrant
DBPASS = secret

db/console:
	$(PSQL) $(DBNAME)

db/create: db/create/user db/create/database db/seed

db/create/database:
	@echo "--> create DB"
	$(PSQL) -c "CREATE DATABASE $(DBNAME) OWNER $(DBUSER);"

db/create/user:
	@echo "--> create DB user"
	$(PSQL) -c "CREATE USER $(DBUSER) WITH PASSWORD '$(DBPASS)';"

pip/freeze:
	@echo "--> saving python dependencies to requirements.txt"
	pip freeze > requirements.txt

pip/update:
	@echo "--> updating python dependencies from requirements.txt"
	pip install -r requirements.txt

venv/setup: venv/setup_venv venv/setup_shell

venv/setup_shell:
	@echo "--> configuring python environment"
	(test -f ~/.bash_profile  && grep venv/bin/activate ~/.bash_profile) || \
		echo "cd $(WORKDIR) && source venv/bin/activate" >> ~/.bash_profile

venv/setup_venv:
	@echo "--> creating python virtual environment"
	test -d venv || python3 -m venv venv