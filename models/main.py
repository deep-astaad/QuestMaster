import streamlit as st
from PyPDF2 import PdfReader
from qa_context import QAContext
# Import the strategy classes
from albert_strategy import AlbertStrategy
from bert_strategy import BertStrategy
from xlnet_strategy import XLNetStrategy
from roberta_strategy import RoBERTaStrategy
from distilbert_strategy import DistilBERTStrategy

def read_pdf(file_path):
    book = PdfReader(file_path)
    text = ""
    for page in book.pages:
        text += page.extract_text()
    return text

def main():
    st.title("Unified LLM Question Answering System")

    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file is not None:
        text = read_pdf(uploaded_file)
        context_text = st.text_area("Context", text, height=300)
        question = st.text_input("Question", "")

        model_choice = st.selectbox("Choose a model", ("ALBERT", "BERT", "XLNet", "RoBERTa", "DistilBERT"))

        strategy_map = {
            "ALBERT": AlbertStrategy(),
            "BERT": BertStrategy(),
            "XLNet": XLNetStrategy(),
            "RoBERTa": RoBERTaStrategy(),
            "DistilBERT": DistilBERTStrategy(),
        }

        qa_context = QAContext(strategy_map[model_choice])

        if st.button("Answer"):
            if context_text and question:
                result = qa_context.perform_qa(context_text, question)
                st.write("Answer:", result["answer"])

if __name__ == "__main__":
    main()