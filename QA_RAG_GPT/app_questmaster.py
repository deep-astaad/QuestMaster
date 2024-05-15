import warnings

warnings.filterwarnings("ignore")

import os
import time
import streamlit as st

# from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings

from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import (
    # CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)

# # from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.document_loaders import TextLoader


# from copy import deepcopy

# from tempfile import NamedTemporaryFile
from tempfile import TemporaryDirectory

# from langchain.docstore.document import Document

from dotenv import load_dotenv

load_dotenv()

from cassandra_connection import create_datastax_connection
from openai_gpt import openai_gpt


def main():
    index_placeholder = True
    st.set_page_config(page_title="QuestMaster", page_icon="💻")
    st.header("QuestMaster: NCERT 📔 QA")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "activate_chat" not in st.session_state:
        st.session_state.activate_chat = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message["avatar"]):
            st.markdown(message["content"])

    session = create_datastax_connection()
    llm = openai_gpt()

    table_name = "questmaster"
    keyspace = "questmaster_keyspace"
    openai_embeddings = OpenAIEmbeddings()

    index_creator = VectorstoreIndexCreator(
        vectorstore_cls=Cassandra,
        embedding=openai_embeddings,
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=30),
        vectorstore_kwargs={
            "session": session,
            "keyspace": keyspace,
            "table_name": table_name,
        },
    )

    with st.sidebar:
        st.subheader("Please Upload File Here")
        docs = st.file_uploader(
            "⬆️ Upload the PDF & Click to Process",
            accept_multiple_files=False,
            type=["pdf"],
        )

        if st.button("Process"):
            with st.spinner("Processing..."):
                time.sleep(1)
                with TemporaryDirectory() as temp_dir:
                    temp_file_path = os.path.join(temp_dir, "tempfile.pdf")
                    with open(temp_file_path, "wb") as f:
                        f.write(docs.getbuffer())

                    with st.spinner("Processing"):
                        loader = PyPDFLoader(temp_file_path)
                        pages = loader.load_and_split()
                        pdf_index = index_creator.from_loaders([loader])
                        # index_placeholder = deepcopy(pdf_index)

                        if "pdf_index" not in st.session_state:
                            st.session_state.pdf_index = pdf_index

                        st.session_state.activate_chat = True

    if st.session_state.activate_chat == True:
        if prompt := st.chat_input("Enter the question..."):
            with st.chat_message("user", avatar="👧🏻"):
                st.markdown(prompt)

            st.session_state.messages.append(
                {"role": "user", "avatar": "👧🏻", "content": prompt}
            )

            index_placeholder = st.session_state.pdf_index
            context_response = index_placeholder.query_with_sources(prompt, llm=llm)
            cleaned_response = context_response["answer"]

            with st.chat_message("assistant", avatar="👨‍💻"):
                st.markdown(cleaned_response)

            st.session_state.messages.append(
                {"role": "assistant", "avatar": "👨‍💻", "content": cleaned_response}
            )

        else:
            st.markdown("Please Upload the PDF to chat.")


if __name__ == "__main__":
    main()
