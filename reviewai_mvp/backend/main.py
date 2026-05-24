from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

class CodeRequest(BaseModel):
    code: str = ""
    repo_url: str = ""

def fetch_github_code(repo_url):

    try:

        repo_path = repo_url.replace(
            "https://github.com/",
            ""
        )

        api_url = f"https://api.github.com/repos/{repo_path}/contents"

        response = requests.get(api_url)

        files = response.json()

        code_content = ""

        for file in files:

            if file["type"] == "file":

                if file["name"].endswith(
                    (".py", ".js", ".java", ".cpp", ".html", ".css")
                ):

                    download_url = file["download_url"]

                    file_data = requests.get(download_url)

                    code_content += f"\n\n# FILE: {file['name']}\n"

                    code_content += file_data.text[:3000]
        print(code_content)
        return code_content

    except Exception as e:
        return str(e)
@app.get("/")
def home():
    return {"message": "ReviewAI Backend Running"}

@app.post("/review")
async def review_code(data: CodeRequest):


    code_to_review = data.code

    if data.repo_url:

        fetched_code = fetch_github_code(data.repo_url)

        if fetched_code.strip():
            code_to_review = fetched_code
    prompt = f"""
    You are a senior software engineer reviewing code.

    Analyze this code for:
    - Bugs
    - Security vulnerabilities
    - Performance issues
    - Code smells

    Return:
    - Severity
    - Issue
    - Explanation
    - Suggested Fix
    - Code Quality Score

    Code:
    {code_to_review}
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "review": response.choices[0].message.content
    }