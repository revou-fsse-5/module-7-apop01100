from app.connections.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Enum
from sqlalchemy.orm import relationship
from datetime import date, datetime, timezone
from app.constants.enums import GenderUsersEnum, RoleUsersEnum
from werkzeug.security import generate_password_hash, check_password_hash

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), default=None, nullable=True)
    email = Column(String(128), nullable=False, unique=True)
    gender = Column(Enum(GenderUsersEnum), nullable=False)
    birth_date = Column(Date, nullable=False)
    username = Column(String(128), nullable=False, unique=True)
    hash_password = Column(String(256), nullable=False)
    role = Column(Enum(RoleUsersEnum), default=RoleUsersEnum.USER.value, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=None, onupdate=datetime.now(timezone.utc), nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=False)
    
    # Relationship Table
    # reviews_relation = relationship("Reviews", back_populates="users")
    
    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)
    
    @property
    def calculated_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    def to_dict(self):
        user = {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "role": self.role,
            "metadata": {
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "is_deleted": self.is_deleted
            }
        }
        
        return user
