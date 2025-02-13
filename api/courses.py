import fastapi

router = fastapi.APIRouter()

@router.get("/courses")
async def get_courses():
    return {"courses": []}

@router.post("/courses")
async def create_course_api():
    return {"courses": []}

@router.get("/courses/{course_id}")
async def get_course(course_id: int):
    return {"courses": []}  

@router.patch("/courses/{course_id}")
async def update_course(course_id: int):
    return {"courses": []}

@router.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    return {"courses": []}
