from fastapi import APIRouter
from app.database import vector_store
import app.services

router = APIRouter()

@router.post("/select-docs/")
async def select_documents(docs: list[str]):
    if docs:
        try:
            filter_ids = {"ids":{"$in":docs}}
            app.services.filter.clear()
            app.services.filter.update(filter_ids)
            selected_docs = vector_store.get(ids=docs)["metadatas"]
            return {"selected_docs": selected_docs}
        except Exception as e:
            return {"response": f"An error occured, {e}"}
        
    else:
        return {"response": "Please provide some valid ids to include.", "selected_docs":[]}
