from knowledgeassistant.logging.logger import logging
from knowledgeassistant.exception.exception import KnowledgeAssistantException

from knowledgeassistant.entity.config_entity import RAGConfig
from knowledgeassistant.utils.main_utils.utils import read_txt_file, write_txt_file

import os
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from together import Together
from langchain.chains import RetrievalQA
from langchain_core.language_models import LLM

from dotenv import load_dotenv
import typing

load_dotenv()
os.environ["TOGETHER_API_KEY"] = os.getenv("TOGETHER_API_KEY")

class RAG:
    def __init__(self, rag_config: RAGConfig):
        try:
            self.rag_config = rag_config
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)
        
    def split_text(self, input_text_path: str):
        try:
            text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
            raw_documents = text_splitter.split_text(text = read_txt_file(file_path = input_text_path))
            documents = [Document(page_content=text) for text in raw_documents]
            return documents
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)
    
    def create_and_store_embeddings(self, documents: list):
        try:
            db = FAISS.from_documents(documents, OllamaEmbeddings(model="nomic-embed-text"))
            return db
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)

    class TogetherLLM(LLM):
        model_name: str = "meta-llama/Llama-3-8b-chat-hf"

        @property
        def _llm_type(self) -> str:
            return "together_ai"

        def _call(self, prompt: str, stop: typing.Optional[typing.List[str]] = None) -> str:
            client = Together()
            response = client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
    
    def retrieval(self, llm, db, query):
        try:
            chain = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=db.as_retriever()
            )
            result = chain.invoke(query)
            return result
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)
    
    def initiate_rag(self, input_text_path: str, query: str):
        try:
            docs = self.split_text(input_text_path = input_text_path)
            store = self.create_and_store_embeddings(documents = docs)
            llm = self.TogetherLLM()
            result = self.retrieval(
                llm = llm,
                db = store,
                query = query
            )
            write_txt_file(
                file_path = self.rag_config.rag_generated_text_path,
                content = result['result']
            )
        except Exception as e:
            raise KnowledgeAssistantException(e, sys)