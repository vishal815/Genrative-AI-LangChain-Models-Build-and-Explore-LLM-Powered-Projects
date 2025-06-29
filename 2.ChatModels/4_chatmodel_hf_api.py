# https://huggingface.co/settings/tokens
# https://huggingface.co/models
# Open source model
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    task='text-generation'
)

result = llm.invoke("what is Genrative ai?")
print(result)                                           # hear we can't able to use object result.content hear






# OR M-2 with ChatHuggingface

# model = ChatHuggingFace(llm=llm)
# result = model.invoke("what is Genrative ai?")
# print(result.content)






# pip install langchain langchain-huggingface huggingface-hub python-dotenv