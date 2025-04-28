import os
import sqlite3

from flask import Flask


ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEMPLATES = os.path.join(ROOT, 'templates')

flaskapp = Flask("BookStore", template_folder=TEMPLATES)
flaskapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database_uri = os.environ.get('SQLITE_URI', ':memory:')

database = sqlite3.connect(database_uri, check_same_thread=False)
cursor = database.cursor()


# Unsafe usage of format()
user_input = "{0.__class__}".format("string")  # This can expose internal details
print(user_input)
