web: gunicorn ECOMERCE_WEB.wsgi --log-file -
##or work good with external database 
web : python manage.py migrate && gunicorn ECOMERCE_WEB.wsgi