from flask import jsonify
from functools import wraps
from flask_jwt_extended import get_jwt, jwt_required

# Custom decorator to check role
def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorated_view(*args, **kwargs):
            current_user = get_jwt()
            if current_user["role"] != role:
                return jsonify({"message": "role not authorized"}), 403
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper