from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    name: str = None  # Имя необязательное
    data: bytes


class ImageCreate(ImageBase):
    name: Optional[str] = None


class ImageDelete(ImageBase):
    id: int


class ImageSchema(ImageBase):
    id: int

    class Config:
        orm_mode = True

class ImageListSchema(BaseModel):
    id: int
    name: str