from fastapi import APIRouter, HTTPException, status

from app.model.resume_model import (
    ResumeRequest,
    ResumeRequestOut,
    ResumeResponseOut,
)
from app.storage import (
    load_resume_requests,
    save_resume_request,
    load_resume_responses,
    save_resume_response,
)
from app.services.request_services import create_and_save_request
from app.services.ai_services import analyze_resume_with_ai
from app.services.response_services import create_and_save_response


resume_router = APIRouter(prefix="/api/v1/resume", tags=["resume"])


@resume_router.get("/")
def read_root():
    return {"message": "Hello, Welcome to the AI Resume Analyzer!"}


@resume_router.get("/requests", response_model=list[ResumeRequestOut])
def get_resume_requests():
    """Get all resume requests"""
    return load_resume_requests()


@resume_router.get("/requests/{request_id}", response_model=ResumeRequestOut)
def get_resume_request(request_id: str):
    """Get a specific resume request by ID"""
    resume_requests = load_resume_requests()
    for req in resume_requests:
        if req["id"] == request_id:
            return req
    raise HTTPException(status_code=404, detail="Resume request not found")


@resume_router.get("/responses", response_model=list[ResumeResponseOut])
def get_resume_responses():
    """Get all resume responses"""
    return load_resume_responses()


@resume_router.get("/responses/{response_id}", response_model=ResumeResponseOut)
def get_resume_response(response_id: str):
    """Get a specific resume response by ID"""
    resume_responses = load_resume_responses()
    for resp in resume_responses:
        if resp["id"] == response_id:
            return resp
    raise HTTPException(status_code=404, detail="Resume response not found")


@resume_router.post(
    "/analyze", response_model=ResumeResponseOut, status_code=status.HTTP_201_CREATED
)
def analyze_resume(resume_request: ResumeRequest):
    """Analyze the resume data and return the results"""

    new_request = create_and_save_request(resume_request)

    ai_response = analyze_resume_with_ai(resume_request)

    print("AI Resume Analysis Result:", ai_response)

    resume_response = create_and_save_response(
        ai_response=ai_response, new_request=new_request
    )

    return resume_response


@resume_router.delete("/requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resume_request(request_id: str):
    """Delete a specific resume request by ID"""
    resume_requests = load_resume_requests()
    resume_responses = load_resume_responses()
    # Also delete associated responses
    updated_responses = [
        resp for resp in resume_responses if resp["request_id"] != request_id
    ]
    save_resume_response(updated_responses)
    updated_requests = [req for req in resume_requests if req["id"] != request_id]

    if len(updated_requests) == len(resume_requests):
        raise HTTPException(status_code=404, detail="Resume request not found")
    save_resume_request(updated_requests)
    return
