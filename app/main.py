from fastapi import FastAPI
from app.routes import ingestion, qa, selection, fetch
import uvicorn

app = FastAPI(title="RAG-based Q&A App")

# Include routes
app.include_router(ingestion.router, prefix="/documents", tags=["Document Ingestion"])
app.include_router(qa.router, prefix="/qa", tags=["Q&A"])
app.include_router(selection.router, prefix="/selection", tags=["Document Selection"])
app.include_router(fetch.router, prefix="/list", tags= ["List Document"])

@app.get("/")
async def root():
    return {"message": "Welcome to RAG-based Q&A API!"}




if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000)