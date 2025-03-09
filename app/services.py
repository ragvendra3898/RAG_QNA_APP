from app.database import vector_store
from langchain_openai import OpenAI, ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata
from app.config import embedding_model, SPLIT_CHUNK_SIZE, CHUNK_OVERLAP
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

filter = {}

def ingest_document(file_path:str):
    """Stores document embeddings in ChromaDB"""
    docs = filter_complex_metadata(UnstructuredFileLoader(file_path).load())
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", "\t"], chunk_size=SPLIT_CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    texts = text_splitter.split_documents(docs)
    num_documents = len(texts)
    print(f"Split file into {num_documents} documents")
    ids = vector_store.add_documents(documents=texts, embedding=embedding_model)
    return ids

def query_rag(question: str, filter=None):
    """Retrieves documents and generates answers using RAG"""
    llm = ChatOpenAI(model='gpt-4o')
    retriever = vector_store.as_retriever(filter=filter)
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return qa_chain.invoke(question)


