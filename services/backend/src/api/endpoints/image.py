import shutil
from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import AsyncSessionLocal, get_async_session
from src.models.image import Image
from src.schemas.image import ImageSchema, ImageCreate
from src.crud.base import CRUDBase


router = APIRouter()

img_crud = CRUDBase(Image)


@router.get("/img", response_model=List[ImageSchema], tags=("IMAGES",))
async def get_all_img(session: AsyncSessionLocal = Depends(get_async_session)):
    img = await img_crud.get_multi(session=session)
    return img

@router.post("/uploadfile/", tags=("IMAGES",))
async def create_img(
    photo: UploadFile = File(...),
    session: AsyncSession = Depends(get_async_session),
):
    try:
        image_data = await photo.read()

        image = Image(name=photo.filename, data=image_data)
        session.add(image)
        await session.commit()

        return {'photo': photo.filename}
    except Exception as e:
        return {'error': str(e)}






