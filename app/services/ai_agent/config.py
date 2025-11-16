
import os
from dotenv import load_dotenv
load_dotenv()

MAX_CHARS = 10_000
MODEL_NAME = "gemini-2.0-flash-001"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")