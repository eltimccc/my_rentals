from pydantic import BaseModel
from fastapi_users import schemas
from typing import Optional

class UserBase(BaseModel):
    full_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]

class UserRead(UserBase, schemas.BaseUser[int]):
    pass

class UserCreate(UserBase, schemas.BaseUserUpdate):
    pass

class UserUpdate(UserBase, schemas.BaseUserUpdate):
    pass
