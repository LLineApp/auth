release: python manage.py migrate
web: gunicorn hackernews.wsgi:application --preload --log-level debug --log-file -
