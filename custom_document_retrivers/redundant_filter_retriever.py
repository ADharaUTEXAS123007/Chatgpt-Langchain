from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma
from langchain.schema import BaseRetriever

class RedundantFilterRetriever(BaseRetriever):
    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        # Calculate embeddings for the query
        emb = self.embeddings.embed_query(query)

        # Perform the query on the vector store, returning the top k results
        return self.chroma.max_marginal_relevance_search_by_vector(embedding=emb, lambda_mult=0.8)

    async def aget_relevant_documents(self, query):
        # Calculate embeddings for the query
        emb = self.embeddings.embed_query(query)

        # Perform the query on the vector store, returning the top k results
        return await self.chroma.asimilarity_search_by_vector(emb, k=5)