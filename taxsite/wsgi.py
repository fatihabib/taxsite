import os
import sys

# Add your project directory to the sys.path
# Replace 'yourusername' with your PythonAnywhere username
path = '/home/fatihabib/tax_automation_site/taxsite'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'taxsite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
