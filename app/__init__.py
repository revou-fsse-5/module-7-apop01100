from flask import Flask, redirect
from app.config import DevelopmentConfig
from app.connections.db import Base, engine
from app.models.users_model import Users
from app.models.review_user_model import Reviews
from app.models.product_model import Product
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from app.config.swagger import swagger_template

jwt = JWTManager()

def create_app(test_config=None):
    app = Flask(__name__)
    
    Base.metadata.create_all(engine, checkfirst=True)
    
    if test_config is not None:
        app.config.from_object(test_config)
    else:
        app.config.from_object(DevelopmentConfig)
        
    jwt.init_app(app)
    swagger = Swagger(app, template=swagger_template)
    
    @app.route("/")
    def index():
        return redirect("/apidocs/#/")
        
    from app.routes import register, login, review, data_control
    app.register_blueprint(register, url_prefix="/register")
    app.register_blueprint(login, url_prefix="/login")
    app.register_blueprint(review, url_prefix="/review")
    app.register_blueprint(data_control, url_prefix="/data")
    
    return app