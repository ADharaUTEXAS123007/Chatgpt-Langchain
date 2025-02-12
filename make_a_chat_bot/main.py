from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

memory = ConversationBufferMemory(chat_memory = FileChatMessageHistory("messages.json"),memory_key="chat_history", return_messages=True)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="chat_history"), #holds the messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(llm=chat, prompt=prompt, memory=memory)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
