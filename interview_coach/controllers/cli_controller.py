from services.interview_service import InterviewService


class CLIController:
    """Very small CLI controller kept simple for readability."""

    def __init__(self):
        self.service = InterviewService()

    def run(self):
        print("\n===== AI MOCK INTERVIEW COACH =====")

        job_role = input("Enter Job Role: ")
        difficulty = input("Enter Difficulty (Easy/Medium/Hard): ")
        print("Starting the Interview Session...\n")

        # messages is a simple list of dicts (system, assistant, user)
        messages = self.service.start_interview(job_role, difficulty)

        # initial AI message (introduction + question)
        ai_message = self.service.get_next_response(messages)
        print("\n" + ai_message)

        while True:
            user_answer = input("\nYour Answer (type 'exit' to quit): ")

            if user_answer.lower() == "exit":
                print("\nInterview Ended. Good luck with your preparation!")
                break

            ai_message = self.service.get_next_response(messages, user_answer)
            print("\n" + ai_message)