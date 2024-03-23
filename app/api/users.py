from fastapi import APIRouter

router = APIRouter()

# base endpoint: /api/user


@router.get("/", tags=["user"])
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/{user_id}", tags=["user"])
async def read_user(user_id: int):
    return {"user_id": user_id, "username": "Foo"}
