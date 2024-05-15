import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from PyPDF2 import PdfReader

def read_pdf(file_path):
    book = PdfReader(file_path)
    text = ""
    for page in book.pages:
        text += page.extract_text()
    return text

# Define each model's perform_qa function
def perform_qa_albert(context, question):
    nlp = pipeline("question-answering", model="mfeb/albert-xxlarge-v2-squad2")
    return nlp(question=question, context=context)

def perform_qa_bert(context, question):
    model_name = "deepset/bert-large-uncased-whole-word-masking-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)
    return nlp(question=question, context=context)

def perform_qa_xlnet(context, question):
    nlp = pipeline("question-answering", model="xlnet-base-cased")
    return nlp(question=question, context=context)

def perform_qa_roberta(context, question):
    nlp = pipeline("question-answering", model="deepset/roberta-base-squad2")
    return nlp(question=question, context=context)

def perform_qa_distilbert(context, question):
    nlp = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    return nlp(question=question, context=context)

def main():
    # Streamlit interface
    st.title("Unified LLM Question Answering System")

    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file is not None:
        text = read_pdf(uploaded_file)
        context = st.text_area("Context", text, height=300)
        question = st.text_input("Question", "")

        model_choice = st.selectbox("Choose a model", ("ALBERT", "BERT", "XLNet", "RoBERTa", "DistilBERT"))

        if st.button("Answer"):
            if context and question:
                if model_choice == "ALBERT":
                    result = perform_qa_albert(context, question)
                elif model_choice == "BERT":
                    result = perform_qa_bert(context, question)
                elif model_choice == "XLNet":
                    result = perform_qa_xlnet(context, question)
                elif model_choice == "RoBERTa":
                    result = perform_qa_roberta(context, question)
                elif model_choice == "DistilBERT":
                    result = perform_qa_distilbert(context, question)
                
                st.write("Answer:", result["answer"])

if __name__ == "__main__":
    main()