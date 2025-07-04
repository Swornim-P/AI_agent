from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time() -> dict  :
    """Get the current time in a specific format YYYY-MM-DD HH:MM:SS."""

    from datetime import datetime
    #return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    } #ADK wraps the return value in a dictionary


root_agent = Agent(
    name="tool_agent",
    model = "gemini-2.0-flash",
    description=("An agent that uses tools to perform tasks."),
    instruction=("You are an agent that can use tools to perform tasks. You provide the current date and time to the user."),
    # The tools that this agent can use
    # In this case, we are using the Google Search tool
    # tools=[
    #     google_search
    # ] 
    tools=[
        get_current_time
   ]
)