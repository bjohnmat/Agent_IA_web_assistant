# agent.py

import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import SerpAPIWrapper
from dotenv import load_dotenv

def load_environment():
    """Charge les clés API depuis le fichier .env"""
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("SERPAPI_API_KEY"):
        raise EnvironmentError("Les clés API sont manquantes dans le fichier .env.")

def get_agent(verbose: bool = True):
    """Crée et retourne un agent LangChain avec un outil de recherche Web."""
    llm = ChatOpenAI(temperature=0, model="gpt-4")

    search = SerpAPIWrapper()
    search_tool = Tool(
        name="Search",
        func=search.run,
        description="Useful for answering questions about current events or facts from the internet."
    )

    return initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent="zero-shot-react-description",
        verbose=verbose
    )
