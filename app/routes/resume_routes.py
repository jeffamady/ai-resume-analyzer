from fastapi import APIRouter, HTTPException, status
from app.model.resume_model import ResumeRequest, ResumeResponse
from app.storage import (
    load_resume_requests,
    save_resume_request,
    load_resume_responses,
    save_resume_response,
)
import uuid

resume_router = APIRouter(prefix="/api/v1/resume", tags=["resume"])


@resume_router.get("/")
def read_root():
    return {"message": "Hello, Welcome to the AI Resume Analyzer!"}


@resume_router.get("/requests", response_model=list[ResumeRequest])
def get_resume_requests():
    """Get all resume requests"""
    return load_resume_requests()


@resume_router.get("/requests/{request_id}", response_model=ResumeRequest)
def get_resume_request(request_id: str):
    """Get a specific resume request by ID"""
    resume_requests = load_resume_requests()
    for req in resume_requests:
        if req["id"] == request_id:
            return req
    raise HTTPException(status_code=404, detail="Resume request not found")


@resume_router.get("/responses", response_model=list[ResumeResponse])
def get_resume_responses():
    """Get all resume responses"""
    return load_resume_responses()


@resume_router.get("/responses/{response_id}", response_model=ResumeResponse)
def get_resume_response(response_id: str):
    """Get a specific resume response by ID"""
    resume_responses = load_resume_responses()
    for resp in resume_responses:
        if resp["id"] == response_id:
            return resp
    raise HTTPException(status_code=404, detail="Resume response not found")


@resume_router.post(
    "/analyze", response_model=ResumeResponse, status_code=status.HTTP_201_CREATED
)
def analyze_resume(resume: ResumeRequest):
    """Analyze the resume data and return the results"""
    resume_requests = load_resume_requests()
    new_request = {
        "id": str(uuid.uuid4()),
        "resume_data": resume.resume_data,
        "job_description": resume.job_description,
    }
    resume_requests.append(new_request)
    save_resume_request(resume_requests)
    # Here use the AI model to analyze the resume and job description, and generate the response

    # When received the AI response, save it to the storage
    resume_response = {
        "id": str(uuid.uuid4()),
        "request_id": new_request["id"],
        "strengths": ["Python", "Data Analysis"],
        "weaknesses": ["Public Speaking"],
        "recommendations": [
            "Consider improving public speaking skills through practice and training.",
        ],
        "missing_skills": ["Project Management", "Communication"],
        "score": 85,
    }

    resume_responses = load_resume_responses()
    resume_responses.append(resume_response)
    save_resume_response(resume_responses)

    return resume_response
