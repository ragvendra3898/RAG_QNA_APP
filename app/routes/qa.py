from fastapi import APIRouter
from app.models import QueryModel
from app.services import query_rag

router = APIRouter()

@router.get("/query/")
async def query_qa(question: str):
    answer = query_rag(question)
    return {"answer": answer}
