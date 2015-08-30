# project/_config.py


import os


# grab the folder where this script lives
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'flasktaskr.db')

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'
DEBUG = False

# define the full path for the database
DATABASE_PATH = os.path.join(BASE_DIR, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
