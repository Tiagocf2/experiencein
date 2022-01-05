# This file contains the WSGI configuration required to serve up your
# web application at http://tiagocf2.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://help.pythonanywhere.com/pages/DebuggingImportError

# +++++++++++ DJANGO +++++++++++
import os
import sys

path = '/home/tiagocf2/experiencein'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'experiencein.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()