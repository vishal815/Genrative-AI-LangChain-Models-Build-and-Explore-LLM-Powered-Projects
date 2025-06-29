# For anthropic api => https://console.anthropic.com/settings/keys
# documentation -> https://docs.anthropic.com/en/docs/about-claude/models/overview
# Not open source model


from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-opus-4-20250514')  #hear also we can able to set temperature and max_comlition token

result= model.invoke("what is GenAI?")

print(result.containt)

