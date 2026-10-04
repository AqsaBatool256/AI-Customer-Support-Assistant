from pathlib import Path

from app.services.vector_store import add_documents


KNOWLEDGE_BASE_PATH = Path("data/knowledge_base.txt")


def load_knowledge_base() -> str:
    """Load the knowledge base from the text file."""
    return KNOWLEDGE_BASE_PATH.read_text(encoding="utf-8")


def build_knowledge_index():
    """Load the knowledge base and add it to ChromaDB."""
    knowledge_base = load_knowledge_base()

    documents = [
        section.strip() for section in knowledge_base.split("\n\n") if section.strip()
    ]

    add_documents(documents)

    print(f"Indexed {len(documents)} documents successfully.")


if __name__ == "__main__":
    build_knowledge_index()
