from fastapi import FastAPI, Path, Query

from api import users, sections, courses

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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
