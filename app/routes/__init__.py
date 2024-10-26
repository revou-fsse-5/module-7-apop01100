from flask import Blueprint
from app.controllers.register_controller import RegisterController
from app.controllers.login_controller import LoginController
from app.controllers.review_controller import reviews_controller, create_user_review_controller
from app.controllers.data_controller import data_controller

register = Blueprint("register", __name__)
login = Blueprint("login", __name__)
review = Blueprint("review", __name__)
data_control = Blueprint("data", __name__)

register.add_url_rule("/<string:role>", view_func=RegisterController.add_user, methods=["POST"])
login.add_url_rule("/", view_func=LoginController.user_login, methods=["POST"])
review.add_url_rule("/admin", view_func=reviews_controller, methods=["GET"])
review.add_url_rule("/user", view_func=create_user_review_controller, methods=["POST"])
data_control.add_url_rule("/", view_func=data_controller, methods=["GET", "POST", "DELETE"])