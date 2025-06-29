# https://platform.openai.com/docs/guides/embeddings
# Not open source model
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large', 
    dimensions= 32
    )

result=embedding.embed_query("Future of genrative AI?")
print(str(result))




# By default, the length of the embedding vector is 1536 for text-embedding-3-small or 3072 for text-embedding-3-larg
# Bigger embedding capture more contextual meaning