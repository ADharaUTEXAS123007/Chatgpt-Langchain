from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from redundant_filter_retriever import RedundantFilterRetriever
import langchain

langchain.debug = True


load_dotenv()

chat = ChatOpenAI(temperature=0)
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="emb", embedding_function=embeddings)

retriever = RedundantFilterRetriever(embeddings=embeddings, chroma=db)

chain = RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever=retriever)

result = chain.run("What is an interesting fact about the English language?")

print(result)