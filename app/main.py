from fastapi import FastAPI

app = FastAPI()


@app.get("/check")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/analyze")
def analyze_resume(resume_data: str):
    """Analyze the resume data and return the results"""
    return {
        "strenghs": ["Python", "Data Analysis"],
        "weaknesses": ["Public Speaking"],
        "recommendations": [
            "Consider improving public speaking skills through practice and training."
        ],
    }
