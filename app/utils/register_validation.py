from pydantic import BaseModel
from datetime import date
from app.constants.enums import GenderUsersEnum, RoleUsersEnum

class RegisterValidation(BaseModel):
    first_name: str
    last_name: str
    email: str
    gender: GenderUsersEnum
    birth_date: date
    username: str
    password: str
    role: RoleUsersEnum