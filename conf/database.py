from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:trootech1234@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = "0lldqz1iPvbPe4K6gId5nXschFYwKdrruWt_8Q9Mn0g"
