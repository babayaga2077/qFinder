from app import app

import random
import string
import os

UPLOAD_FOLDER = 'app/uploads/'

app.secret_key=''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(32))
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'toor'
app.config['MYSQL_DATABASE_DB'] = 'quotes'
app.config['MYSQL_DATABASE_HOST'] = 'db'
