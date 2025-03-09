# RAG-based Q&A System

## Overview
The **RAG-based Q&A System** is a **Retrieval-Augmented Generation (RAG)** application that enables users to upload documents, retrieve relevant content, and generate AI-powered answers based on selected documents.

This application is built using **FastAPI**, **LangChain**, **ChromaDB**, and **OpenAI's LLMs** for efficient document ingestion, retrieval, and question answering.

## Features of The App
- **Document Ingestion**: Upload documents and store embeddings for retrieval.
- **Q&A System**: Ask questions, and retrieve context-aware AI-generated answers.
- **Document Selection**: Specify which documents to use for answering queries.
- **List Documents**: Fetch all stored documents for reference.

## Setup
### 1. Clone the Repository
```bash
git clone <repository-url>
cd rag_qna_app
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv rag_env
source rag_env/bin/activate  # On macOS/Linux
rag_env\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn app.main:app --reload
```

### 4. API Documentation
Access interactive API docs at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Deployment
### Build and Run with Docker
```bash
docker build -t rag-app .
docker-compose up
```

## API Endpoints
| Method | Endpoint | Description |
|--------|-------------|-------------------------------|
| **POST** | `/documents/upload/` | Upload a document & store embeddings |
| **GET** | `/qa/query/` | Ask a question and retrieve an AI-generated answer from indexed docs|
| **POST** | `/selection/select-docs/` | Select specific documents for retrieval |
| **GET** | `/list/all/` | Fetch all stored documents |
| **GET** | `/` | Welcome message |

## File Structure
```
rag_qna_app/
│── app/
│   ├── __init__.py
│   ├── main.py            # Main FastAPI app
│   ├── database.py        # ChromaDB initialization
│   ├── config.py          # Configuration settings
│   ├── models.py          # Pydantic models
│   ├── services.py        # Business logic
│   ├── routes/
│   │   ├── ingestion.py   # Document ingestion API
│   │   ├── qa.py          # Q&A API
│   │   ├── selection.py   # Document selection API
│   │   ├── fetch.py       # List stored documents
│── tests/
|   |test_files/
|   ├── state_of_the_union.txt
│   ├── test_ingestion.py  # Unit test for ingestion
│   ├── test_qa.py         # Unit test for Q&A API
│── Dockerfile             # Docker containerization
│── docker-compose.yml     # Multi-container setup
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

## Running Tests
To run unit tests:
```bash
python -m pytest tests/ --disable-warnings
```

## Contributing
Feel free to fork this repository, open an issue, or submit a pull request! 

## License
This project is licensed under the **MIT License**.

