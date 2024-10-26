import os

class Config:
    SECRET_KEY  = os.getenv("SECRET_KEY")

class DevelopmentConfig():
    DEBUG = True
    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
    
class TestConfig():
    TESTING = True