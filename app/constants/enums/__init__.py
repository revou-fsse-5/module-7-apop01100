from enum import Enum

class GenderUsersEnum(str, Enum):
    MALE = "male"
    FEMALE = "female"
    
class RoleUsersEnum(str, Enum):
    ADMIN = "admin"
    SUPER_ADMIN = "super admin"
    USER = "user"
    
    @classmethod
    def get_all_values(cls):
        roles = list(cls)
        roles_value = [role.value for role in roles]
        
        return roles_value
