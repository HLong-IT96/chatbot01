# run/run_ingest.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.ingest import load_documents, split_documents

if __name__ == "__main__":
    print("🔄 Loading documents...")
    docs = load_documents()
    print(f"✅ Loaded {len(docs)} raw documents")

    print("✂️ Splitting into chunks...")
    chunks = split_documents(docs)
    print(f"✅ Created {len(chunks)} chunks")

    print("🎉 Ingest done!")
