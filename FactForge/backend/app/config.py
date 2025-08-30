import os
from dotenv import load_dotenv
BASE_DIR = os.path.dirname(__file__)
env = os.path.join(BASE_DIR, ".env")
if os.path.exists(env):
    load_dotenv(env)
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-fast")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "240"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./factforge.db")
WIKIPEDIA_USER_AGENT = os.getenv("WIKIPEDIA_USER_AGENT", "FactForge/1.0 (contact@example.com)")
