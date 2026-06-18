from fastapi import FastAPI
from app.routes.resume_routes import resume_router

app = FastAPI()

app.include_router(resume_router)
