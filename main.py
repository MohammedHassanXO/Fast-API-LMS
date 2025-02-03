from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="LMS API",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact={
        "name": "Moahmmed Hassan",
        "email": "MohammedHassanXO@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

users = []
class User(BaseModel):
    name: str
    age: int
    bio: Optional[str] = None


@app.post("/user")
async def create_user(user: User):
    users.append(user)
    return "User created successfully"

@app.get("/user", response_model=List[User])
async def get_users():
    return users

@app.get("/user/{user_id}")
async def get_users(
    user_id: int=Path(..., description="The ID of the user you want to view", gt=1),
    q: str = Query(None, max_length=5)
):
    return {"User": users[user_id], "Query": q}
