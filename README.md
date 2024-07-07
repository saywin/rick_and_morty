# Rick & Morty

### Requirements:
1. Endpoint, which return random character from the world of Rick and Morty series.
2. Endpoint get search_string as an argument and return list of all characters, who contains the search_string in the name.
3. On regular basis, app downloads data from external service to inner DB.
4. Requests of implemented API should work with local DB (Take data from DB not from Rick & Morty API).

### Technologies to use:
1. Public API: https://rickandmortyapi.com/documentation.
2. Use Celery as task scheduler for data synchronization for Rick & Morty API.
3. Python, Django/Flask/FastAPI, ORM, PostgreSQL, Git.
4. All endpoints should be documented via Swagger.

# How to run:
- Create venv: `python -m venv venv`
- Activate it: `.\venv\Scripts\Activate.ps1`
- Install requirements: `pip install -r requirements.txt`
- Run migrations: `pip manage.py migrate`
- Run Redis server: `docker run -d -p 6379:6379 redis`
- Run celery worker for task handling: `celery -A rick_and_morty_api worker -l INFO --pool=solo`
- Run celery beat for task scheduling: `celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
- Create schedule for running sync in BD
- Run app: `python manage.py runserver`
