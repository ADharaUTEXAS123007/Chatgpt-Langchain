from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

load_dotenv()

embeddings = OpenAIEmbeddings()

# emb = embeddings.embed_query("Hi, there!")

# print(emb)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
documents = loader.load_and_split(text_splitter=text_splitter)

# calculate all embeddings from documents
db = Chroma.from_documents(documents, embeddings, persist_directory="emb")

results = db.similarity_search_with_score("What is an interesting fact about the English language?")

for result in results:
    print("\n")
    print(result[1])
    print(result[0].page_content)

