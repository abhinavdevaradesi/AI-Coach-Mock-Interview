# AI Coach Mock Interview

A command-line mock interview coach powered by [Ollama](https://ollama.com) and local LLMs (default: `llama3.2`). It conducts realistic, role-specific interviews, asks one question at a time, and evaluates each answer with a score, strengths, areas for improvement, and an ideal answer — before moving to the next question.

## Features

- Interactive CLI interview flow
- Customizable job role and difficulty level (Easy / Medium / Hard)
- One question at a time, no spoilers before you answer
- Structured evaluation after every response: score, strengths, gaps, ideal answer, and next question
- Runs entirely locally via Ollama — no API keys, no external services
- Clean, modular architecture (controllers, services, models, utils)

## Project Structure

```
interview_coach/
├── controllers/
│   └── cli_controller.py      # CLI input/output loop
├── models/
│   └── interview.py            # Initial message state for a session
├── services/
│   └── interview_service.py    # Orchestrates prompts and Ollama calls
├── utils/
│   └── ollama_client.py        # Thin wrapper around the Ollama chat API
├── main.py                     # Entry point
├── prompts.py                  # System prompt template
└── requirements.txt
```

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com) installed and running locally
- A pulled model (default `llama3.2`):

  ```bash
  ollama pull llama3.2
  ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/ai-coach-mock-interview.git
   cd ai-coach-mock-interview/interview_coach
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure Ollama is running in the background:

   ```bash
   ollama serve
   ```

## Usage

Run the application from the `interview_coach` directory:

```bash
python main.py
```

You'll be prompted to enter:

1. **Job Role** — e.g. `Backend Developer`, `Data Analyst`, `Product Manager`
2. **Difficulty** — `Easy`, `Medium`, or `Hard`

The interviewer will introduce itself and ask the first question. Type your answer and press Enter to receive an evaluation and the next question. Type `exit` at any time to end the session.

### Example Session

```
===== AI MOCK INTERVIEW COACH =====
Enter Job Role: Backend Developer
Enter Difficulty (Easy/Medium/Hard): Medium
Starting the Interview Session...

INTERVIEWER:
Hi, I'm your AI interview coach for this session...
What is the difference between SQL and NoSQL databases, and when would you choose one over the other?

Your Answer (type 'exit' to quit): SQL databases are relational...

EVALUATION:
Score: 7/10

Strengths:
- Correctly identified relational vs non-relational structure
- Mentioned use cases

Areas for Improvement:
- Could mention scalability tradeoffs (vertical vs horizontal)

Ideal Answer:
...

Next Question:
...
```

## Configuration

By default, the app uses the `llama3.2` model. To use a different model, update the model name in `services/interview_service.py`:

```python
self.client = OllamaClient(model="your-model-name")
```

## How It Works

- `prompts.py` builds a system prompt that defines the interviewer's persona, rules, difficulty guidelines, and required output format.
- `models/interview.py` initializes the conversation with that system prompt.
- `services/interview_service.py` manages the conversation state, appending user answers and AI responses while delegating the actual model call to `OllamaClient`.
- `utils/ollama_client.py` wraps the `ollama.chat()` call.
- `controllers/cli_controller.py` handles all terminal I/O and drives the interview loop.

## Roadmap

- [ ] Save interview transcripts to a file
- [ ] Add a final summary report at the end of the session
- [ ] Support multiple LLM backends (OpenAI, Anthropic, etc.)
- [ ] Web-based UI

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with a clear description of the change.

## License

This project is licensed under the MIT License.
