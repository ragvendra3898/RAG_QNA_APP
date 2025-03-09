from fastapi import APIRouter, UploadFile, HTTPException
from app.services import ingest_document
from app.config import UPLOAD_DIR
import os
import shutil

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile):
    try:
        fn = f"{UPLOAD_DIR}/{file.filename.lower()}"
        with open(fn, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        return {"response": f"There was an error processing the file '{file.filename}', {str(e)}."}
    finally:
        file.file.close()
    try:
        ids = ingest_document(fn)
        os.remove(fn)
        return {"message": "Document uploaded successfully", "doc_id":ids}
    except Exception as e:
        return {"message": f"An error occured while indexing file, {e}"}
