release: python manage.py migrate
web: gunicorn auth.wsgi:application --preload --log-level debug --log-file -
