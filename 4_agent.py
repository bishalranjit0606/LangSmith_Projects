import os
import requests
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langsmith import Client

os.environ["LANGCHAIN_PROJECT"] = "agent"

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in .env file")

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  access_key = os.getenv("WEATHERSTACK_API_KEY")
  if not access_key:
    return "WEATHERSTACK_API_KEY not found in .env file"

  url = f"https://api.weatherstack.com/current?access_key={access_key}&query={city}"

  response = requests.get(url)
  response.raise_for_status()

  return str(response.json())

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = Client().pull_prompt(
    "hwchase17/react",
    dangerously_pull_public_prompt=True,
)
prompt.template += (
    "\nAfter Action Input, stop. Do not write Observation yourself. "
    "Wait for the tool result, then write Thought and Final Answer.\n"
)

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True,
    max_iterations=5,
    handle_parsing_errors=True,
)

# What is the release date of Dhadak 2?
# What is the current temp of gurgaon
# Identify the birthplace city of Kalpana Chawla (search) and give its current temperature.

# Step 5: Invoke
response = agent_executor.invoke({"input": "indefity the birthoplace of gautam buddha and current temoeratiur of kathmandu"})
print(response)

print(response['output'])