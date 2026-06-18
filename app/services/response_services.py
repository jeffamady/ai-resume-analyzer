from app.storage import (
    load_resume_responses,
    save_resume_response,
)
from app.model.resume_model import ResumeResponse, ResumeResponseOut, ResumeRequestOut
import uuid


def create_and_save_response(
    ai_response: ResumeResponse,
    new_request: ResumeRequestOut,
) -> ResumeResponseOut:
    resume_responses = load_resume_responses()
    new_resume_response = {
        "id": str(uuid.uuid4()),
        "request_id": new_request["id"],
        "strengths": ai_response["strengths"],
        "weaknesses": ai_response["weaknesses"],
        "recommendations": ai_response["recommendations"],
        "missing_skills": ai_response["missing_skills"],
        "score": ai_response["score"],
        "professional_summary": ai_response["professional_summary"],
    }
    resume_responses.append(new_resume_response)
    save_resume_response(resume_responses)
    return new_resume_response
