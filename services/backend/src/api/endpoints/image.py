import shutil
from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, Response, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.image import ImageListSchema

from src.core.db import AsyncSessionLocal, get_async_session
from src.models.image import Image
from src.schemas.image import ImageSchema, ImageCreate
from src.crud.base import CRUDBase


router = APIRouter()

img_crud = CRUDBase(Image)


@router.get("/all", response_model=List[ImageListSchema])
async def get_all_img(session: AsyncSession = Depends(get_async_session)):
    img_list = await img_crud.get_multi(session=session)

    img_with_name_id = [{"id": img.id, "name": img.name} for img in img_list]

    return img_with_name_id


@router.get("/get_img/{image_id}", response_model=ImageSchema)
async def get_image(
    image_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    image = await img_crud.get(session=session, obj_id=image_id)
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(content=image.data, media_type="image/jpeg")


@router.post("/uploadfile/")
async def create_img(
    photo: UploadFile = File(...),
    session: AsyncSession = Depends(get_async_session),
):
    try:
        image_data = await photo.read()

        await img_crud.create(
            session=session, obj_in=ImageCreate(name=photo.filename, data=image_data)
        )

        return {"photo": photo.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
