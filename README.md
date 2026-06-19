# AI Resume Analyzer Project

AI Resume Analyzer is a FastAPI-based backend application that leverages OpenAI structured outputs to evaluate resumes against job descriptions.

The application analyzes candidate profiles, identifies strengths and weaknesses, provides recommendations, and stores request and response history.

## Features

* Resume analysis using OpenAI
* Job description matching
* Structured responses with Pydantic models
* Persistent request and response storage
* Request and response retrieval by ID
* Cascading delete functionality
* JSON-based storage
* RESTful API endpoints
* Automatic API documentation through Swagger UI

## Technologies

* Python
* FastAPI
* OpenAI API
* Pydantic
* UV
* Uvicorn

## Project Structure

```text
app/
├── main.py
├── storage.py
├── data/
├── models/
├── routes/
├── services/
└── utils/
```

## Quick Start

Clone repository
   ```bash
   git clone https://github.com/jeffamady/ai-resume-analyzer.git
   ```

Install dependencies:
   ```text
   uv sync
   ```

Create a .env file:

```text
OPENAI_API_KEY=your_api_key_here
```

Start the application:

```bash
cd app
uvicorn main:app --reload
```

Access Swagger documentation:

```text
http://localhost:8000/docs
```

## Example Request

```json
{
  "resume_data": "...",
  "job_description": "..."
}
```

## Endpoints

### GET /

Welcome message
<img width="1138" height="893" alt="image" src="https://github.com/user-attachments/assets/952e7039-9b51-4431-bff1-62638e377792" />

### POST /api/v1/resume/analyze

Analyze a resume against a job description.
<img width="1136" height="883" alt="image" src="https://github.com/user-attachments/assets/d1ce3325-f2c4-4db6-9641-e7157dd18e54" />


### GET /api/v1/resume/requests

Retrieve all requests.
<img width="1126" height="899" alt="image" src="https://github.com/user-attachments/assets/61831cd4-2fc2-4615-8f7d-3b2cb4a740de" />


### GET /api/v1/resume/requests/{id}

Retrieve a request by ID.
<img width="1132" height="906" alt="image" src="https://github.com/user-attachments/assets/de617c5e-dd0f-4eaf-875f-4874e38e3651" />

### GET /api/v1/resume/responses

Retrieve all AI responses.
<img width="1128" height="901" alt="image" src="https://github.com/user-attachments/assets/aaa57d34-cdb5-40c5-a253-11fbd8033f1d" />

### GET /api/v1/resume/responses/{id}

Retrieve a response by ID.
<img width="1137" height="779" alt="image" src="https://github.com/user-attachments/assets/4804694d-81c1-47af-bcef-b32ac071ee1f" />

### DELETE /api/v1/resume/requests/{id}

Delete a request and its associated AI response.
<img width="1129" height="832" alt="image" src="https://github.com/user-attachments/assets/3a7b3638-9b04-4aa6-817d-ae122f24f8ad" />

## Future Improvements

* Database integration with PostgreSQL
* Docker support
* Unit testing
* Authentication and authorization
* Frontend application
* Streamlit dashboard
* Vector database support
* Semantic resume search
* Deployment to Render or Railway
* CI/CD pipelines using GitHub Actions
