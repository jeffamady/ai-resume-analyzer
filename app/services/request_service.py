from app.storage import (
    load_resume_requests,
    save_resume_request,
)
from app.model.resume_model import ResumeRequest, ResumeRequestOut
import uuid


class RequestService:
    def create_and_save_request(
        self, resume_request: ResumeRequest
    ) -> ResumeRequestOut:
        resume_requests = load_resume_requests()
        new_request = {
            "id": str(uuid.uuid4()),
            "resume_data": resume_request.resume_data,
            "job_description": resume_request.job_description,
        }
        resume_requests.append(new_request)
        save_resume_request(resume_requests)
        return new_request
