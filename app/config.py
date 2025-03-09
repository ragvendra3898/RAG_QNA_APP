import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding_model = OpenAIEmbeddings()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-api-key")
CHROMA_DB_PATH = os.path.join(os.getcwd(), "chroma_db")
UPLOAD_DIR = os.path.join(os.getcwd(), "files")
os.makedirs(UPLOAD_DIR, exist_ok=True)
SPLIT_CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
