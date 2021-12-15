from config import *
from flask import Flask
from flask_mysql_connector import MySQL
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()

def create_app(test_config = None):
    
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY      = SECRET_KEY,
        MYSQL_DATABASE  = DB_NAME,
        MYSQL_HOST      = DB_HOST,
        MYSQL_USER      = DB_USERNAME,
        MYSQL_PASSWORD  = DB_PASSWORD
    )
    
    mysql.init_app(app)
    CSRFProtect(app)
    
    from .student import student
    from .course import course
    app.register_blueprint(student)
    app.register_blueprint(course)
    
    return app