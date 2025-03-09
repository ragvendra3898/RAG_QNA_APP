from fastapi import APIRouter
from app.database import vector_store
router = APIRouter()

@router.get("/get_documents/")
async def list_chroma_docs():
    data = vector_store.get()["metadatas"]
    return list({frozenset(d.items()): d for d in data}.values())