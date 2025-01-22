import os
import langchain
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from qdrant_client import QdrantClient

# Initialize the language model with specific settings
OLLAMA_SERVER = os.getenv("OLLAMA_SERVER")

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_SERVER"),
    model = "llama3.2:latest",
    temperature = 0.8
)

groq = ChatGroq(
    temperature=0, 
    model_name="mixtral-8x7b-32768"
)

vdb = QdrantClient(host='lawboxai_qdrant')

