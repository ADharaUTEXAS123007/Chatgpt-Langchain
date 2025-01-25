from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationSummaryMemory, FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

memory = ConversationSummaryMemory(memory_key="chat_history", return_messages=True, llm=chat)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(llm=chat, prompt=prompt, memory=memory, verbose=True)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
