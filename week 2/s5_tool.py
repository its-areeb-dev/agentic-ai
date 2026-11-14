
import sys
sys.path.insert(0, r'C:\Users\PC-2B-14\Downloads\agentic ai\week 1')

from agents import Agent, Runner, function_tool
from llm import model


# Create a function tool
@function_tool
def get_weather(city: str) -> str:
    """
    Get weather information for a city.
    """
    return f"The weather in {city} is sunny with 30 degree temperature."


INSTRUCTIONS = """
You are a helpful AI assistant.
You can use tools to answer user questions.
If user asks about weather, use the get_weather tool.
Explain answers briefly.
"""


# Create Agent
agent = Agent(
    name='ToolAgent',
    instructions=INSTRUCTIONS,
    model=model,
    tools=[get_weather]
)


# Run Agent
while True:
    user_input = input('You: ')

    if user_input.lower() == 'quit':
        break

    result = Runner.run_sync(agent, user_input)

    print(f'Agent: {result.final_output}')
