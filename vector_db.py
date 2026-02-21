from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from config import EMBEDDING_MODEL

embedding = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL)

VECTOR_DB_DIR = "chroma"
COLLECTION_NAME = "rag_collection"


def create_vector_store(chunks):
    """
    Recreates collection safely without deleting folder.
    """

    # Initialize Chroma client
    vectordb = Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embedding,
        collection_name=COLLECTION_NAME
    )

    # 🔥 Delete existing collection safely
    try:
        vectordb.delete_collection()
    except:
        pass

    # Recreate new collection
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=VECTOR_DB_DIR,
        collection_name=COLLECTION_NAME
    )

    return vectordb


def load_vector_store():
    return Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embedding,
        collection_name=COLLECTION_NAME
    )