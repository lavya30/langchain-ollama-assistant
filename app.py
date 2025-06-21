import os
from dotenv import load_dotenv
import streamlit as slt
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("human", "Question: {question}")
    ]
)

slt.title("Gemma AI")
input_text = slt.text_input("What question do you have in mind:")

# Ollama model
llm = Ollama(model="gemma3:1b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    slt.write(chain.invoke({"question": input_text}))
