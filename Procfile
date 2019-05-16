web: gunicorn notebook.wsgi

web: python Notebook/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT Notebook/settings.py 


