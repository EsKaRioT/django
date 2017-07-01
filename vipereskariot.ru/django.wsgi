import os, sys

virtual_env = '/var/www/test'
activate_this = os.path.join(virtual_env, 'bin/activate_this.py')
exec(open(activate_this).read())

sys.path.insert(0, "/var/www/domains/django")
sys.path.insert(0, "/var/www/domains/django/newproject")
sys.path.insert(0, "/var/www/test/lib/python3.4")
sys.path.insert(0, "/var/www/test/lib/python3.4/site-packages")

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
