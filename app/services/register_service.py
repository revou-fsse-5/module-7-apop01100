from flask import jsonify
from app.connections.db import Session
from app.models.users_model import Users


class RegisterService:
    @staticmethod
    def add_user(data):
        with Session() as session:
            try:
                new_user: Users = Users(
                    first_name = data["first_name"],
                    last_name = data["last_name"],
                    email = data["email"],
                    gender = data["gender"],
                    birth_date = data["birth_date"],
                    username = data["username"],
                    role=data["role"]
                )
                new_user.set_password(data["password"])
                
                session.add(new_user)
                session.commit()
            except Exception as e:
                session.rollback()
                return jsonify({
                    "error": f"{e}"
                }), 400
            
            return jsonify({
                "message": "success add new user",
                "new_user": new_user.to_dict()
                }), 201