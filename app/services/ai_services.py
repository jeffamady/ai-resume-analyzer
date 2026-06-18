from app.model.resume_model import (
    ResumeRequest,
    ResumeResponse,
)
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume_with_ai(resume_request: ResumeRequest) -> ResumeResponse:
    """Analyze the resume using OpenAI's GPT-5.5 model"""
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

    content = ai_resume_response.output_parsed

    return parse_ai_response(content)


def parse_ai_response(content) -> ResumeResponse:
    return {
        "strengths": content.strengths,
        "weaknesses": content.weaknesses,
        "recommendations": content.recommendations,
        "missing_skills": content.missing_skills,
        "score": content.score,
        "professional_summary": content.professional_summary,
    }
