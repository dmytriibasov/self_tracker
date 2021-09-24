app:
		@mkdir -p src/apps/$(name)
		@python src/manage.py startapp $(name) src/apps/$(name)

server:
		@python src/manage.py runserver

migrations:
		@python src/manage.py makemigrations

migrate:
		@python src/manage.py migrate

createsuperuser:
		@python src/manage.py createsuperuser

# Celery


# Postgres commands
postgres:
	sudo -u postgres psql

