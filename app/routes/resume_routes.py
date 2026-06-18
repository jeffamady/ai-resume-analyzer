from fastapi import APIRouter, HTTPException, status
from app.model.resume_model import ResumeRequest, ResumeResponse

resume_router = APIRouter(prefix="/api/v1/resume", tags=["resume"])


@resume_router.get("/")
def read_root():
    return {"message": "Hello, Welcome to the AI Resume Analyzer!"}


@resume_router.post(
    "/analyze", response_model=ResumeResponse, status_code=status.HTTP_201_CREATED
)
def analyze_resume(resume: ResumeRequest):
    """Analyze the resume data and return the results"""
    # print("Received resume data:", payload.resume_data)
    # print("Received job description:", payload.job_description)
    resume_response = {
        "strengths": ["Python", "Data Analysis"],
        "weaknesses": ["Public Speaking"],
        "recommendations": [
            "Consider improving public speaking skills through practice and training.",
        ],
        "missing_skills": ["Project Management", "Communication"],
        "score": 85,
    }
    return resume_response
