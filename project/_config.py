# project/_config.py


import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'E\xf37z*\xd0\x96\xea}[\xea\xe2\xcad;\xd2_\xd3\x02\xc1\x98M\xf5'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
