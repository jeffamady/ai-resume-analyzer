from pydantic import BaseModel


class ResumeRequest(BaseModel):
    resume_data: str
    job_description: str


class ResumeAnalysisResponse(BaseModel):
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]
    missing_skills: list[str]
    score: int
