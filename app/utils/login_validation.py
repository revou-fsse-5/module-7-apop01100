from pydantic import BaseModel

class LoginValidation(BaseModel):
    username: str
    password: str