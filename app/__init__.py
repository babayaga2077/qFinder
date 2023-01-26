from flask import Flask
from flaskext.mysql import MySQL
import socket
import logging

app = Flask(__name__)

from app import config

mysql = MySQL()
mysql.init_app(app)

from app import routes