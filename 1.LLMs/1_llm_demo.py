from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Create OpenAI LLM object
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Invoke the LLM with a prompt
result = llm.invoke("What is the capital of India?")

# Print result
print(result)


