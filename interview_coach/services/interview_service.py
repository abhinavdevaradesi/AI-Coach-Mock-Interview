from utils.ollama_client import OllamaClient
from prompts import get_system_prompt
from models.interview import create_initial


class InterviewService:
    """A small, easy-to-read service that mirrors the original script logic.

    - start_interview returns a simple messages list
    - get_next_response appends the user's answer (if any), calls the client,
      appends the assistant response and returns it
    """

    def __init__(self, model="llama3.2"):
        self.client = OllamaClient(model=model)

    def start_interview(self, job_role, difficulty):
        system_prompt = get_system_prompt(job_role, difficulty)
        return create_initial(job_role, difficulty, system_prompt)

    def get_next_response(self, messages, user_answer=None):
        if user_answer is not None:
            messages.append({"role": "user", "content": user_answer})

        ai_message = self.client.chat(messages)
        messages.append({"role": "assistant", "content": ai_message})
        return ai_message