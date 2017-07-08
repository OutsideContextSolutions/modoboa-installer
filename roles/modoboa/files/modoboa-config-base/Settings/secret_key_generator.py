import os
try:
    from .secret_key import *
except ImportError:
    from django.utils.crypto import get_random_string
    SETTINGS_DIR=os.path.abspath(os.path.dirname(__file__))
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, chars)

    secretfile = open(SETTINGS_DIR+"/secret_key.py", 'w')
    secretfile.write("SECRET_KEY = \'"+secret_key+"\'\n")
    secretfile.close()
from .secret_key import SECRET_KEY
