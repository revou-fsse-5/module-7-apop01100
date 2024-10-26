from flask import request, jsonify
from app.services.register_service import RegisterService
from app.utils.register_validation import RegisterValidation
from flasgger import swag_from
from pydantic import ValidationError

class RegisterController:
    @staticmethod
    @swag_from("../docs/register_api_doc.yaml")
    def add_user(role):
        allowed_roles = {"admin", "user"}
        if role not in allowed_roles:
            return jsonify({
                "message": "role not exist"
            }), 400
            
        data = request.json
        data["role"] = role
        
        try:
            register_valid = RegisterValidation.model_validate(data)
        except ValidationError as e:
            return jsonify({
                "message": f"{e}"
            }), 400
            
        response = RegisterService.add_user(register_valid.model_dump())
        
        return response