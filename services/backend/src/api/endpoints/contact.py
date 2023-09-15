from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.contact import ContactCreate, ContactSchema, ContactUpdate
from src.core.db import get_async_session
from src.crud.contact import contact_crud

router = APIRouter()


@router.get("/{contact_id}", response_model=ContactSchema)
async def get_contact_by_id(
    contact_id: int, session: AsyncSession = Depends(get_async_session)
):
    try:
        contact = await contact_crud.get(obj_id=contact_id, session=session)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        return contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[ContactSchema])
async def get_all_contacts(session: AsyncSession = Depends(get_async_session)):
    contacts = await contact_crud.get_multi(session=session)
    return contacts


@router.post("/", response_model=ContactSchema)
async def create_contact(
    contact_data: ContactCreate, session: AsyncSession = Depends(get_async_session)
):
    try:
        contact = await contact_crud.create(obj_in=contact_data, session=session)
        return contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{contact_id}", response_model=ContactSchema)
async def update_contact(
    contact_id: int,
    contact_data: ContactUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        contact = await contact_crud.get(obj_id=contact_id, session=session)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")

        updated_contact = await contact_crud.update(
            db_obj=contact, obj_in=contact_data, session=session
        )
        return updated_contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{contact_id}", response_model=ContactSchema)
async def patch_contact(
    contact_id: int,
    contact_data: ContactUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        contact = await contact_crud.get(obj_id=contact_id, session=session)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")

        patched_contact = await contact_crud.patch(
            db_obj=contact, obj_in=contact_data, session=session
        )
        return patched_contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{contact_id}", response_model=ContactSchema)
async def delete_contact(
    contact_id: int, session: AsyncSession = Depends(get_async_session)
):
    try:
        contact = await contact_crud.get(obj_id=contact_id, session=session)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")

        deleted_contact = await contact_crud.remove(db_obj=contact, session=session)
        return deleted_contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
