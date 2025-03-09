from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingestion():
    response = client.post("/documents/upload/", files={"file": ("test.txt", b"Sample text")})
    assert response.status_code == 200
    assert "doc_id" in response.json()
