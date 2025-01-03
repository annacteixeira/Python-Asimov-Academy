import os
from dotenv import load_dotenv
from pathlib import Path

from langchain_community.llms import OpenAI
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

from configs import *

import streamlit as st


FILES_FOLDER = Path(__file__).parent / 'files'

def initialize_api_openai():
    load_dotenv()
    llm = OpenAI(model='gpt-3.5-turbo-instruct')
    
    return llm

def document_loading():
    docs = []
    for file in FILES_FOLDER.glob('*.pdf'):
        loader = PyPDFLoader(file)
        docs_file = loader.load()
        docs.extend(docs_file)
    
    return docs

def document_splitting(docs):
    recur_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2500,
        chunk_overlap=250,
        separators=['\n\n', '\n', '.', ' ', '']
    )
    
    docs = recur_splitter.split_documents(docs)
    
    for i, doc in enumerate(docs):
        doc.metadata['source'] = doc.metadata['source'].split('/')[-1]
        doc.metadata['doc_id'] = i
        
    return docs

def create_vector_store(docs):
    embedding_model = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(
        documents=docs,
        embedding=embedding_model
    )
    
    return vector_store

def create_conversation_chain():
    
    docs = document_loading()
    docs = document_splitting(docs)
    vector_store = create_vector_store(docs)
    
    chat = ChatOpenAI(model=get_config('model_name'))
    
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key='chat_history',
        output_key='answer'
    )
    
    retriever = vector_store.as_retriever(
        search_type = get_config('retrieval_search_type'),
        search_kwargs = get_config('retrieval_kwargs')
    )
    
    prompt_template = PromptTemplate.from_template(get_config('prompt'))
    
    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory=memory,
        return_source_documents=True,
        retriever=retriever,
        combine_docs_chain_kwargs={'prompt': prompt_template},
        verbose=True
    )
    
    st.session_state['chain'] = chat_chain

if __name__ == '__main__':
    initialize_api_openai()
    
