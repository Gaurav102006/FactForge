
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(BASE_DIR, ".env")
if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_FACTCHECK_API_KEY = os.getenv("GOOGLE_FACTCHECK_API_KEY", "")
WIKIPEDIA_USER_AGENT = os.getenv("WIKIPEDIA_USER_AGENT", "FactForge/1.0")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
