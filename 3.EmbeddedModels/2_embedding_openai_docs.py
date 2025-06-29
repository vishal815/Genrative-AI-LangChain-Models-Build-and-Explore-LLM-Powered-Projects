# https://platform.openai.com/docs/guides/embeddings
# its not open source model
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions= 32)

dcoutments= [
    "what is Genrative Ai?",
    "What is Ai Agent?",
    "what is AgenticAI?"
]

result=embedding.embed_documents("Future of genrative AI?")
print(str(result))



# embed_documents =to pass multiple documents