from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

###############################
users = []
class User(BaseModel):
    name: str
    age: int
    bio: Optional[str] = None
###############################

@router.post("/user")
async def create_user(user: User):
    users.append(user)
    return "User created successfully"

@router.get("/user", response_model=List[User])
async def get_users():
    return users

@router.get("/user/{user_id}")
async def get_users(user_id: int):
    return users[user_id]
