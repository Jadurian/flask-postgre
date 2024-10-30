import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/students_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
