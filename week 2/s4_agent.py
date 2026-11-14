import sys
sys.path.insert(0, r'C:\Users\PC-2B-14\Downloads\agentic ai\week 1')

from agents import Agent, Runner
from llm import model

INSTRUCTIONS = 'You are a helpful code assistant. Write clean, simple Python code. Explain briefly.'

agent = Agent(name='CodeAssistant', instructions=INSTRUCTIONS, model=model)

while True:
    user_input = input('You: ')
    if user_input.lower() == 'quit':
        break
    result = Runner.run_sync(agent, user_input)
    print(f'Agent: {result.final_output}')