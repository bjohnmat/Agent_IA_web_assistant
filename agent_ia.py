#%%

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import SerpAPIWrapper
import os

import loadenv

# 🔐 Set API keys
os.environ["OPENAI_API_KEY"] = "your openai key"
os.environ["SERPAPI_API_KEY"] = "you google search key"
# GPT model
llm = ChatOpenAI(temperature=0, model="gpt-4")

# Define the tool
search = SerpAPIWrapper()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Useful for answering questions about current events or facts from the internet"
)

# Create a reactive agent that uses the search tool
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

query = input("Ask me anything: ")
response = agent.run(query)
print("\n🤖 Agent Response:\n", response)