from pathlib import Path
import json

DATA_DIR = Path("app/data")
DATA_FILE_REQ = DATA_DIR / "resumes_requests.json"
DATA_FILE_RES = DATA_DIR / "resumes_responses.json"


def load_resume_requests():
    """Load resume requests from the JSON file"""
    if DATA_FILE_REQ.exists():
        with open(DATA_FILE_REQ, "r") as f:
            content = f.read()
            if content.split():
                return json.loads(content)
    return []


def save_resume_request(resume_request):
    """Save the resume request data to a JSON file"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE_REQ, "w") as f:
        json.dump(resume_request, f, indent=2)


def load_resume_responses():
    """Load resume responses from the JSON file"""
    if DATA_FILE_RES.exists():
        with open(DATA_FILE_RES, "r") as f:
            content = f.read()
            if content.split():
                return json.loads(content)
    return []


def save_resume_response(resume_response):
    """Save the resume response data to a JSON file"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE_RES, "w") as f:
        json.dump(resume_response, f, indent=2)
