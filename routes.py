from fastapi import APIRouter

from dbconfig import check_db

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    await check_db()
    return {"item_id": item_id, "name": f"Item {item_id}"}


@router.post("/items/")
async def create_item(item: dict):
    return {"message": "Item created", "item": item}
