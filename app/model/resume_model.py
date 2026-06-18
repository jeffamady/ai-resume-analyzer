from pydantic import BaseModel


class ResumeRequest(BaseModel):
    resume_data: str
    job_description: str


class ResumeRequestOut(BaseModel):
    id: str
    resume_data: str
    job_description: str


class ResumeResponse(BaseModel):
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]
    missing_skills: list[str]
    score: int
    professional_summary: str


class ResumeResponseOut(BaseModel):
    id: str
    request_id: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]
    missing_skills: list[str]
    score: int
    professional_summary: str
