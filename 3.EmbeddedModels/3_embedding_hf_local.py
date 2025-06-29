# Open source model
# huggingface -> models ->sentence-transformers -> all_MiniLM-L6-v2
# This model we can use throw infrence API but due to small model we are using throw download


from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bihar",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(str(vector))





# for local download and run
# pip install sentence-transformers