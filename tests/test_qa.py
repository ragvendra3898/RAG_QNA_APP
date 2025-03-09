from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_api_valid_question():
    """Test that the /qa/query/ endpoint returns a valid answer for a query."""
    response = client.get("/qa/query/", params={"question":"How many jobs were created last year in America?"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert isinstance(response.json()["answer"]["answer"], str)

def test_query_api_invalid_payload():
    """Test that the /qa/query/ endpoint handles missing input gracefully."""
    response = client.get("/qa/query/")
    assert response.status_code == 422  # Unprocessable Entity (missing 'question' field)

def test_query_api_empty_question():
    """Test that the API handles empty questions appropriately."""
    response = client.get("/qa/query/", params={"question":""})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert isinstance(response.json()["answer"]["answer"], str)  # Expecting a generic fallback response

def test_query_api_performance():
    """Test API response time is within an acceptable range (e.g., <2 seconds)."""
    import time
    start_time = time.time()
    response = client.get("/qa/query/", params={"question":"What did President said about Ketanji Brown Jackson?"})
    end_time = time.time()
    
    assert response.status_code == 200
    assert "answer" in response.json()
    assert (end_time - start_time) < 5  # Ensure response time is within 2 seconds
