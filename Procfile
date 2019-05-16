web: gunicorn notebook.wsgi

web: python Satchel/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT Satchel/settings.py 


