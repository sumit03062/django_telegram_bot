Django API Project with JWT, Celery, and Telegram Bot
This project demonstrates a Django backend setup with the following features:

Features
RESTful API using Django REST Framework

JWT authentication (login, protected routes)

Celery with Redis for background tasks (e.g., sending emails)

Telegram bot integration to store user Telegram usernames

Secure environment variable handling using .env

How to Run
Clone the project and create a virtual environment

Install dependencies:

nginx
Copy code
pip install -r requirements.txt
Create a .env file and add your secret key and Telegram bot token

Run migrations and create a superuser:

nginx
Copy code
python manage.py migrate
python manage.py createsuperuser
Start Redis server

Run Django server:

nginx
Copy code
python manage.py runserver
Run Celery worker:

nginx
Copy code
celery -A myproject worker --loglevel=info
Start the Telegram bot:

nginx
Copy code
python run_bot.py
Endpoints
/api/public/ – Public API

/api/protected/ – Requires JWT token

/api/token/ – Get access and refresh tokens

Requirements
Python 3.8+

Django

djangorestframework

celery

redis

python-telegram-bot

python-decouple

