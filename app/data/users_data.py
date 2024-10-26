from datetime import datetime, date, timezone
from app.models.users_model import Users
from app.constants.enums import GenderUsersEnum, RoleUsersEnum

# Sample users data
users_data = [
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice.smith@example.com",
        "gender": GenderUsersEnum.FEMALE,
        "birth_date": date(1990, 5, 10),
        "username": "alice90",
        "role": RoleUsersEnum.USER,
        "password": "hashpassword1"
    },
    {
        "first_name": "Bob",
        "last_name": "Johnson",
        "email": "bob.johnson@example.com",
        "gender": GenderUsersEnum.MALE,
        "birth_date": date(1985, 11, 20),
        "username": "bob85",
        "role": RoleUsersEnum.USER,
        "password": "hashpassword2"
    },
    {
        "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie.brown@example.com",
        "gender": GenderUsersEnum.MALE,
        "birth_date": date(1995, 1, 30),
        "username": "charlie95",
        "role": RoleUsersEnum.USER,
        "password": "hashpassword3"
    },
    {
        "first_name": "John",
        "last_name": "Wick",
        "email": "johnwick@example.com",
        "gender": GenderUsersEnum.MALE,
        "birth_date": date(1964, 9, 2),
        "username": "BabaYaga",
        "role": RoleUsersEnum.ADMIN,
        "password": "26milliondollars"
    },
    {
        "first_name": "John",
        "last_name": "Cena",
        "email": "johncena@example.com",
        "gender": GenderUsersEnum.MALE,
        "birth_date": date(1995, 1, 30),
        "username": "tettenettet",
        "role": RoleUsersEnum.ADMIN,
        "password": "jedagjedug"
    }
]
