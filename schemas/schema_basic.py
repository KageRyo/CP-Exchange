from enum import Enum
from typing import Optional
from ninja import Schema


class RoleEnum(str, Enum):
    ANONYMOUS = "anonymous"
    NORMAL = "normal"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"
class BasicAuthSchema(Schema):
    username: str
    password: str
    
class RefreshSchema(Schema):
    refresh: str
    
class JWTPairSchema(Schema):
    refresh: str
    access: str
    
class BasicUserSchema(Schema):
    id: int
    username: str
    
class UserSchema(Schema):
    id: id
    username: str
    nickname: Optional[str]
    role: RoleEnum
    is_active: bool

    