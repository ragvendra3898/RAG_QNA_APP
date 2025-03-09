from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_select_documents_valid():
    """Test selecting documents that exist in the database."""
    # Mock some documents
    doc_ids = ["925ae42a-2829-45e2-852e-111e7c11c220","411b6836-8bf5-4209-8b2f-dc47eeb48faa","5cff03a5-294a-4e1d-9d0c-41b2a4fca894"]
    
    response = client.post("/selection/select-docs/", json=doc_ids)
    
    assert response.status_code == 200
    assert "selected_docs" in response.json()
    assert isinstance(response.json()["selected_docs"], list)

def test_select_documents_invalid():
    """Test selecting documents that do not exist in the database."""
    doc_ids = ["123ae42a-2829-45e2-852e-111e7c11c560"]

    response = client.post("/selection/select-docs/", json=doc_ids)

    assert response.status_code == 200  # It should return a valid response, but empty list
    assert "selected_docs" in response.json()
    assert response.json()["selected_docs"] == []

def test_select_documents_empty_list():
    """Test selecting an empty document list."""
    response = client.post("/selection/select-docs/", json=[])
    
    assert response.status_code == 200
    assert "selected_docs" in response.json()
    assert response.json()["selected_docs"] == []
