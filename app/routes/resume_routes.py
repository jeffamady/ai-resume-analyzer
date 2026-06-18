from fastapi import APIRouter, HTTPException, status

# # todo jna remove after
# import sys
import os

# # Add project root to path
# sys.path.insert(0, os.chdir("../.."))
# os.chdir("../..")

# # Verify it worked
# print(os.getcwd())

from app.model.resume_model import (
    ResumeRequest,
    ResumeRequestOut,
    ResumeResponse,
    ResumeResponseOut,
)
from app.storage import (
    load_resume_requests,
    save_resume_request,
    load_resume_responses,
    save_resume_response,
)
import uuid
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


resume_router = APIRouter(prefix="/api/v1/resume", tags=["resume"])

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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
    resume_requests = load_resume_requests()
    new_request = {
        "id": str(uuid.uuid4()),
        "resume_data": resume_request.resume_data,
        "job_description": resume_request.job_description,
    }
    resume_requests.append(new_request)
    save_resume_request(resume_requests)
    # Here use the AI model to analyze the resume and job description, and generate the response
    system_prompt = """
    You are a professional recruiter.

    Analyze the provided resume and evaluate it objectively.

    Return:

    - strengths: list[str]
    - weaknesses: list[str]
    - recommendations: list[str]
    - missing_skills: list[str]
    - score: int (0-100)
    - professional_summary: str

    Scoring Guidelines:

    90-100 : Excellent resume
    80-89  : Strong resume
    70-79  : Good resume
    60-69  : Needs improvement
    0-59   : Weak resume

    Be concise and practical.
    """
    user_prompt = f"""Resume Data:
        {resume_request.resume_data}    

        Job Description:
    {resume_request.job_description}

"""

    ai_resume_response = client.responses.parse(
        model="gpt-5.5",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        text_format=ResumeResponse,
    )

    ai_resume = ai_resume_response.output_parsed

    print("AI Resume Analysis Result:", ai_resume)

    # When received the AI response, save it to the storage
    resume_response = {
        "id": str(uuid.uuid4()),
        "request_id": new_request["id"],
        "strengths": ai_resume.strengths,
        "weaknesses": ai_resume.weaknesses,
        "recommendations": ai_resume.recommendations,
        "missing_skills": ai_resume.missing_skills,
        "score": ai_resume.score,
        "professional_summary": ai_resume.professional_summary,
    }

    resume_responses = load_resume_responses()
    resume_responses.append(resume_response)
    save_resume_response(resume_responses)

    return resume_response
