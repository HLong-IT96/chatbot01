# run/app.py

import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.qa import build_qa_chain

# --- Khởi tạo QA chain 1 lần duy nhất ---
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = build_qa_chain()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

qa_chain = st.session_state.qa_chain

# --- Giao diện UI ---
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Trợ Lý Ảo AI phòng khám da liễu Bác Loan")
st.markdown("Chào bạn!")

# --- Chat input ---
query = st.chat_input("🔎 Nhập câu hỏi của bạn...")

if query:
    with st.spinner("Đang xử lý..."):
        result = qa_chain(query)
        answer = result["result"]
        st.session_state.chat_history.append((query, answer))

# --- Hiển thị lịch sử hội thoại ---
for q, a in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)
