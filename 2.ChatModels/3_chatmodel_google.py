# for api => https://ai.google.dev/ 
# https://ai.google.dev/gemini-api/docs?authuser=2

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model =ChatGoogleGenerativeAI(model='mistralai/Mistral-7B-Instruct-v0.2')

result= model.invoke("what is GenAI?")

print(result)