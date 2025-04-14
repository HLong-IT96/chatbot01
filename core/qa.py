# core/qa.py

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.chains import LLMChain

from langchain.chains import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQAWithSourcesChain

from core.llm_router import get_llm

CHROMA_DIR = "data/vectorstores"

def load_vectorstore():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

def build_qa_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = get_llm()

    # Prompt tiếng Việt
    QA_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        Bạn là một trợ lý AI chuyên nghiệp, luôn trả lời bằng tiếng Việt rõ ràng và dễ hiểu.
        Dựa vào thông tin sau, hãy trả lời câu hỏi:
        
        Thông tin:
        {context}
        
        Câu hỏi: {question}
        Trả lời bằng tiếng Việt:
        """
    )

    # Build LLMChain
    llm_chain = LLMChain(llm=llm, prompt=QA_PROMPT)

    # Build StuffDocumentsChain theo kiểu mới
    stuff_chain = StuffDocumentsChain(
        llm_chain=llm_chain,
        document_variable_name="context"
    )

    # Kết hợp với RetrieverQA
    qa_chain = RetrievalQA(
        retriever=retriever,
        combine_documents_chain=stuff_chain,
        return_source_documents=True
    )

    return qa_chain
