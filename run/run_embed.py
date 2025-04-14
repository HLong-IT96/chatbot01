# run/run_embed.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.ingest import load_documents, split_documents
from core.vectorstore import save_to_vectorstore

if __name__ == "__main__":
    print("📄 Loading and splitting documents...")
    docs = split_documents(load_documents())
    print(f"✅ Got {len(docs)} chunks")

    print("📦 Saving to vectorstore...")
    save_to_vectorstore(docs)
