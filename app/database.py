import chromadb
from langchain_chroma import Chroma
from app.config import CHROMA_DB_PATH, embedding_model


# Initialize ChromaDB Client
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
vector_store = Chroma(client=chroma_client, embedding_function=embedding_model, collection_name="langchain")