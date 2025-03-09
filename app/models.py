from pydantic import BaseModel

class DocumentUpload(BaseModel):
    filename: str
    content: str

class QueryModel(BaseModel):
    question: str
