from operator import itemgetter

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain.vectorstores import FAISS

from scrapper import Scrapper
from prompts import prompt
from typing import *

class RAG():

    def __init__(self) -> None:
        self.scrapper = Scrapper()

    def __get_all_text(self, url):
        return self.scrapper.parse(url)

    def __initialize_vector_store(self, paragraph_texts, openai_api_key):
        vectorstore = FAISS.from_texts(paragraph_texts, OpenAIEmbeddings(openai_api_key=openai_api_key))
        retriever = vectorstore.as_retriever()
        return retriever
    
    def initialize(self, compliance_url, url_to_check, openai_api_key):
        paragraph_texts = self.__get_all_text(compliance_url)
        self.retriever = self.__initialize_vector_store(paragraph_texts, openai_api_key)
        self.texts_to_check = ' '.join(self.__get_all_text(url_to_check))
        self.chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | prompt
            | ChatOpenAI(openai_api_key=openai_api_key)
            | StrOutputParser()
        )

    def format(self, text):
        text = text.replace("\\", '').replace('\n', '').replace('\t', '')
        return text
    
    def run(self):
        if isinstance(self.texts_to_check, list):
            return [self.format(self.chain.invoke(i)) for i in self.texts_to_check]
        else:
            return self.format(self.chain.invoke(self.texts_to_check))
