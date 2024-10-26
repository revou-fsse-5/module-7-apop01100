from app.models.users_model import Users
from app.connections.db import Session
from app.constants.messages import LoginMessages


class LoginService:
    @staticmethod
    def login_user(data):
        username = data["username"]
        password = data["password"]
        
        with Session() as session:
            try:
                user_check: Users = session.query(Users).filter(Users.username == username).first()
                if user_check is None:
                    return LoginMessages.USERNAME_NOT_FOUND
                
                if user_check.check_password(password):
                    return {
                            "access": LoginMessages.SUCCESS["access"],
                            "role": user_check.role,
                            "message": LoginMessages.SUCCESS["message"]
                        }
                else:
                    return LoginMessages.INCORRECT_PASSWORD
            except Exception as e:
                return LoginMessages.error_message(e)
            