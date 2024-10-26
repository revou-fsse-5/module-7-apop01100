class LoginMessages():
    USERNAME_NOT_FOUND = {"access": False, "message": "username not found"}
    INCORRECT_PASSWORD = {"access": False, "message": "incorrect password"}
    SUCCESS = {"access": True, "message": "login succes"}
    
    @staticmethod
    def error_message(error):
        return {"access": False, "message": f"{error}"}