import chromadb


client = chromadb.PersistentClient(path="data/chroma_db")

collection = client.get_or_create_collection(name="novatech_support")


def add_documents(documents: list[str]):
    """Add knowledge-base documents to the vector store."""
    ids = [f"doc_{i}" for i in range(len(documents))]

    collection.upsert(
        ids=ids,
        documents=documents,
    )


def search_documents(query: str, limit: int = 3):
    """Search the vector store for relevant documents."""
    results = collection.query(
        query_texts=[query],
        n_results=limit,
    )

    return results["documents"][0]
