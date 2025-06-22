import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
MAX_CHARS = 10_000
AGENT_MAX_ITERATIONS = 20
MODEL_NAME = "gemini-2.0-flash-001"
SYSTEM_PROMPT = """

"""