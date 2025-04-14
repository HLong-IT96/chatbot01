# core/ingest.py

import os
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

DOCS_FOLDER = "data/documents/phongkham"

def load_documents():
    docs = []
    for filename in os.listdir(DOCS_FOLDER):
        file_path = os.path.join(DOCS_FOLDER, filename)
        if os.path.isfile(file_path):
            loader = UnstructuredFileLoader(file_path)
            loaded = loader.load()
            docs.extend(loaded)
    return docs

def split_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)
