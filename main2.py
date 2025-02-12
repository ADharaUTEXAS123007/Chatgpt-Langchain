#First lines of code
from langchain.llms import OpenAI


llm = OpenAI(openai_api_key=api_key)
result = llm("Tell me a joke")
print(result)
