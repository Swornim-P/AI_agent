from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model = "gemini-2.0-flash",
    description=("An agent that greets the user."),
    instruction=("You are a friendly agent that greets the user warmly. You ask for their name and greet them by their name."),
)