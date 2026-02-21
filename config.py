import os
from dotenv import load_dotenv

load_dotenv()


# Groq API key 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
SIMILARITY_THRESHOLD = 0.75