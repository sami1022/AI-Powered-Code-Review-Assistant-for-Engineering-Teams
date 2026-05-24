# 🚀 ReviewAI

## AI-Powered Code Review Assistant for Engineering Teams

ReviewAI is an AI-powered GitHub code review assistant that analyzes repositories and code snippets in real time to detect:

- Security vulnerabilities
- Performance bottlenecks
- Code quality issues
- Optimization opportunities

It provides intelligent recommendations, analytics dashboards, repository insights, and interactive visualizations using AI.

---

# 📌 Problem Statement

Developers spend hours manually reviewing pull requests, and important bugs, security vulnerabilities, and performance issues are often missed.

ReviewAI automates this process using AI by analyzing repositories and generating intelligent code review feedback instantly.

---

# ✨ Features

✅ AI-powered code review

✅ GitHub repository analysis

✅ Security vulnerability detection

✅ Performance issue detection

✅ Code quality scoring

✅ Interactive analytics dashboard

✅ Repository insights

✅ AI-generated recommendations

✅ Dynamic charts and visualizations

✅ Modern SaaS-style UI

✅ Pull request simulation dashboard

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Chart.js

## Backend
- Python
- FastAPI

## AI
- OpenRouter API
- Large Language Models (LLMs)

## APIs
- GitHub API

---

# 📂 Project Structure

```bash
reviewai/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│
├── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sami1022/AI-Powered-Code-Review-Assistant-for-Engineering-Teams
```

---

## 2️⃣ Open Project Folder

```bash
cd reviewai
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

---

## 4️⃣ Activate Virtual Environment

### PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### CMD

```bash
.venv\Scripts\activate.bat
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# 🔑 API Setup

Get your OpenRouter API key from:

https://openrouter.ai/

---

## Add API Key in `main.py`

```python
client = OpenAI(
    api_key="YOUR_OPENROUTER_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)
```

---

# ▶️ Run Backend Server

Go to backend folder:

```bash
cd backend
```

Run FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Server runs at:

```bash
http://127.0.0.1:8000
```

---

# 🌐 Run Frontend

Open:

```bash
frontend/index.html
```

in your browser.

---

# 🧠 How It Works

## Step 1
User pastes:
- GitHub repository URL
OR
- source code

---

## Step 2
Frontend sends request to FastAPI backend.

---

## Step 3
Backend:
- fetches repository code using GitHub API
- sends code to AI model

---

## Step 4
AI analyzes:
- security vulnerabilities
- performance issues
- code smells
- code quality

---

## Step 5
Results are displayed in:
- interactive dashboard
- charts
- analytics panels
- AI recommendation sections

---

# 📊 Dashboard Modules

## 🚀 Pull Request Review
AI-generated code review results.

## 🛡️ Security Analysis
Security vulnerability insights and charts.

## ⚡ Performance Metrics
Performance analytics dashboard.

## 📂 Repository Insights
Repository statistics and complexity overview.

## 🤖 AI Suggestions
Smart AI-generated recommendations.

---

# 📈 Charts Included

✅ Doughnut Security Chart

✅ Performance Metrics Visualization

✅ Security Severity Analytics

---

# 🚀 Example Use Cases

- AI code review automation
- GitHub repository scanning
- Pull request analysis
- Secure coding analysis
- Engineering productivity tools
- DevOps automation dashboards

---

# 🔮 Future Improvements

- Real GitHub Pull Request integration
- Multi-file repository crawling
- CI/CD integration
- Team collaboration
- PDF report export
- AI-generated PR comments
- Advanced security scanning
- Real-time monitoring

---

# 📸 Screenshots

## Dashboard
(Add screenshot here)

## Security Analysis
(Add screenshot here)

## Performance Metrics
(Add screenshot here)

---

# 🎥 Demo Video

(Add demo video link here)

---

# 👨‍💻 Author

Built for Hackathon Submission 🚀

---

# ⭐ Final Note

ReviewAI demonstrates how AI can automate engineering workflows by improving pull request reviews, security analysis, and developer productivity using modern AI-powered tooling.
