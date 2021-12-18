from config import *
from flask import Flask
from flask_mysql_connector import MySQL
from flask_wtf.csrf import CSRFProtect
import cloudinary
import cloudinary.uploader

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
    
    cloudinary.config(
        CLOUD_NAME  = CLOUD_NAME,
        API_KEY     = API_KEY,
        API_SECRET  = API_SECRET
    )
    
    mysql.init_app(app)
    CSRFProtect(app)
    
    from .student import student
    from .course import course
    from .college import college
    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)
    
    return app