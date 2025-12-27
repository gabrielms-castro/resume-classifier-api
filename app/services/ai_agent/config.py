
import os
from dotenv import load_dotenv
load_dotenv()

MAX_CHARS = 10_000
MODEL_NAME = os.getenv("GEMINI_MODEL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")