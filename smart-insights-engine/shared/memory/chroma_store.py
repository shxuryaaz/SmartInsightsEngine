from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings  # latest package

embedding = OpenAIEmbeddings()

vectorstore = Chroma(
    collection_name="support-tickets",
    embedding_function=embedding,
    persist_directory="./chroma"  # uses local Chroma DB
)

def query_memory(query):
    results = vectorstore.similarity_search(query, k=3)
    return [r.page_content for r in results]
