
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

# Wrap with ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# Invoke the model
result = model.invoke("Difference between Generative AI and Agentic AI?")
print(result.content)




# this require huge amount of communal power to run locally