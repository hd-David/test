import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://postgres:mimi@localhost/test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False