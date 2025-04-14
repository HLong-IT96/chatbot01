# run/run_qa.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.qa import build_qa_chain

if __name__ == "__main__":
    qa_chain = build_qa_chain()

    print("🤖 Ask your question (type 'exit' to quit):")
    while True:
        query = input("🔎 You: ")
        if query.lower() == "exit":
            break
        result = qa_chain(query)
        print(f"\n🧠 Answer: {result['result']}\n")

