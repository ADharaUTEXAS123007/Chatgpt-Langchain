#First lines of code
from langchain.llms import OpenAI

# SECURE THIS KEY !!
api_key = "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"

llm = OpenAI(openai_api_key=api_key)
result = llm("Tell me a joke")
print(result)
