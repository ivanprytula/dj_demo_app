"""
Main idea of such configuration is to use default "python manage.py runserver"
in 'production by default' mode without need of changing manage.py

If you have development.py then try/except will handle settings "swapping"
"""
import sys

from .common import *
from .production import *

try:
    from .development import *
except ImportError:
    sys.exit(1)
