"""
Simple, beginner-friendly InterviewSession helper.

This module provides a very small helper that returns the initial
messages list used by the rest of the application. It's intentionally
kept simple (plain lists and dicts) so it resembles a beginner script.
"""

def create_initial(job_role, difficulty, system_prompt):
    """Return the initial messages list for an interview session.

    Keeps the same structure used by the Ollama API: a list of
    dicts with `role` and `content` keys.
    """
    return [{"role": "system", "content": system_prompt}]
