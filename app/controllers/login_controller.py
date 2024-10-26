from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.services.login_service import LoginService
from app.utils.login_validation import LoginValidation
from flasgger import swag_from
from pydantic import ValidationError

class LoginController:
    @staticmethod
    @swag_from("../docs/login_api_doc.yaml")
    def user_login():
        data = request.json
        
        try:
            login_validated = LoginValidation.model_validate(data)
        except ValidationError as e:
            return jsonify({
                "message": f"{e}"
            }), 400
            
        response = LoginService.login_user(login_validated.model_dump())
        
        if response["access"] == False:
            return jsonify({
                "error": response["message"]
            }), 401
            
        access_token = create_access_token(identity=data["username"], additional_claims={
            "role": response["role"]
        })
        
        return jsonify({
            "message": response["message"],
            "access_token": access_token
        }), 201
        
        
