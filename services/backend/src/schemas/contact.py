from pydantic import BaseModel


class ContactBase(BaseModel):
    email: str
    phone: str
    phone2: str
    vk: str
    address: str
    description: str


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class ContactSchema(ContactBase):
    id: int

    class Config:
        orm_mode = True
