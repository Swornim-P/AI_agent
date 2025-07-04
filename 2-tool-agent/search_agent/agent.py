from google.adk.agents import Agent
from google.adk.tools import google_search




root_agent = Agent(
    name="tool_agent",
    model = "gemini-2.0-flash",
    description=("An agent that can surf the web and provide information based on search results."),
    instruction=("You are an agent that can use tools to perform tasks. Your only job is to search google and provide the search results."),
    # The tools that this agent can use
    # In this case, we are using the Google Search tool
    tools=[
        google_search
    ] 
    
)