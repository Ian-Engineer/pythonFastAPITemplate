from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_users():
    return {"users": 'heres a list for ya'}

@router.get('/users/{user_id}') # path parameters
async def get_user(user_id: int):
    return {"user_id": user_id}

@router.get('/users/sorted/')
async def get_sorted_users(skip: int = 0, limit: int = 10):
    return {'skip': skip, "limit": limit}
