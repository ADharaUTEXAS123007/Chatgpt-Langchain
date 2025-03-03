#Here I learnt how to consider SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import argparse

load_dotenv()


parser = argparse.ArgumentParser()

parser.add_argument("--task", default="return a list of numbers", type=str)
parser.add_argument("--language", default="python", type=str)
args = parser.parse_args()


llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)

test_prompt = PromptTemplate(
    template="Write a test for the following {language} code {code}",
    input_variables=["language", "code"]
)

code_chain = LLMChain(llm=llm, prompt=code_prompt, output_key="code")
test_chain = LLMChain(llm=llm, prompt=test_prompt, output_key="test")

chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["task", "language"],
    output_variables=["test", "code"]
)

#llm = OpenAI(openai_api_key=api_key)
#result = llm("Tell me a joke")


result = chain({"language":args.language, "task":args.task})

print(">>>>Generated code>>>")

print(result["code"])

print(">>>>Generate test>>>>")

print(result["test"])
