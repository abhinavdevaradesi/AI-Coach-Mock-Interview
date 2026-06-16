# AI Coach Mock Interview

Lightweight, layered Python application that runs interactive mock interviews using an LLM via the Ollama client.

This README explains how to run the CLI locally and describes deployment options if you want to expose the app as a web service.

Project structure

```
interview_coach/
├─ controllers/
│  └─ cli_controller.py        # CLI entry for running an interview session
├─ models/
│  └─ interview.py             # creates the initial prompt messages
├─ services/
│  └─ interview_service.py     # orchestrates session state and calls to LLM client
├─ utils/
│  └─ ollama_client.py         # wrapper for `ollama.chat(...)`
├─ main.py                     # app entrypoint that instantiates CLIController
├─ prompts.py                  # system prompt template used to instruct the model
├─ requirements.txt            # dependencies (contains `ollama`)
└─ README.md
```

Core features
- Interactive mock interview loop via the command line
- Role and difficulty-specific prompts (see `prompts.py`)
- Clean, beginner-friendly architecture (controllers / services / models / utils)

Prerequisites
- Python 3.10+ (3.11 recommended)
- Pip for installing Python packages
- Ollama runtime and desired model installed locally (this project uses `llama3.2` by default)

Quick start (Windows PowerShell)

1. Create and activate a virtual environment (optional but recommended):

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

2. Install Python dependencies:

```powershell
python -m pip install -r .\\interview_coach\\requirements.txt
```

3. Make sure Ollama is installed and the model is available (example pulls `llama3.2`):

```powershell
# install/pull model according to Ollama docs, example:
# ollama pull llama3.2
```

4. Run the CLI application:

```powershell
python .\\interview_coach\\main.py
```

Usage
- When running the CLI, you'll be prompted for Job Role and Difficulty (Easy/Medium/Hard).
- The AI prints an introduction + first question. Type your answer and press Enter.
- Type `exit` to quit the interview.

Key files
- `prompts.py` — system prompt template. Edit to change the interview style, rules, or output format.
- `utils/ollama_client.py` — thin wrapper that calls `ollama.chat(...)`. Replace this to use a different provider.
- `controllers/cli_controller.py` — CLI loop. Easy to adapt into a web endpoint.

Deployment options — can I deploy this online?
Yes. The recommended path depends on whether you want to continue using Ollama (self-hosted model) or switch to a hosted LLM provider.

Option A — Run on a remote VM / VPS (keeps Ollama local)
- Provision a Linux VM (DigitalOcean, AWS EC2, Linode).
- Install Ollama and pull the model on that VM.
- Clone this repo, install Python deps and run the app or run a web wrapper (FastAPI) to expose an HTTP API.

High-level steps (Ubuntu example):

```bash
# on your VM
git clone <repo-url>
cd "AI Coach Mock Interview"/interview_coach
python -m venv .venv; source .venv/bin/activate
pip install -r requirements.txt
# install and run Ollama (follow Ollama docs) and pull the model
python main.py
```

Option B — Containerize and deploy
- Build a Docker image for the Python app and run it on a host that can access Ollama.
- If Ollama runs on the host, configure networking so the container can reach the Ollama API.

Example Dockerfile (app only):

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY interview_coach/ ./interview_coach
RUN pip install --no-cache-dir -r interview_coach/requirements.txt
CMD ["python", "interview_coach/main.py"]
```

Option C — Convert to a web app (FastAPI) and host it
- Add a small HTTP API (`web_app.py`) that calls `InterviewService` and stores sessions in memory or a small DB.
- Containerize the web app and deploy to a cloud container service (Railway, Fly, DigitalOcean App Platform, AWS ECS).

Minimal FastAPI sketch (not included in repo by default):

```python
# web_app.py
from fastapi import FastAPI
from pydantic import BaseModel
from services.interview_service import InterviewService

app = FastAPI()
service = InterviewService()
sessions = {}

class StartRequest(BaseModel):
    job_role: str
    difficulty: str

@app.post('/start')
def start(req: StartRequest):
    messages = service.start_interview(req.job_role, req.difficulty)
    sid = str(len(sessions) + 1)
    sessions[sid] = messages
    ai_message = service.get_next_response(messages)
    return {'session_id': sid, 'message': ai_message}
```

Option D — Use a hosted LLM API instead of Ollama
- Replace `utils/ollama_client.py` with a client that calls a hosted API (OpenAI, Anthropic, etc.).
- This allows you to deploy the app anywhere without running Ollama, but it introduces API costs and requires secure key management.

Security & operational notes
- Do not expose Ollama admin interfaces publicly without access control.
- For a public web deployment add authentication, rate-limiting and logging.
- Keep API keys and secrets in environment variables and never commit them.

Troubleshooting
- `ModuleNotFoundError: No module named 'ollama'` — install the package or run in mock mode (if implemented).
- `Model not found` — ensure the Ollama model (e.g. `llama3.2`) is pulled into the Ollama runtime on the machine running the app.

Contributing
- Pull requests welcome. Suggestions:
  - Add a small `web/` example with `docker-compose` that shows Ollama + app networking.
  - Add unit tests around the interview flow.

License
- Add a `LICENSE` file if you intend to publish under a specific license (MIT is common for small projects).

