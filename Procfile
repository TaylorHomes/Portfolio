web: gunicorn notebook.wsgi

web: python notebook/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT notebook/settings.py 
