from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


loader = TextLoader('../state_of_the_union.txt', encoding='utf8')


index = VectorstoreIndexCreator().from_loaders([loader])

query = "What did the president say about Ketanji Brown Jackson"
index.query(query)

query = "What did the president say about Ketanji Brown Jackson"
index.query_with_sources(query)

index.vectorstore

index.vectorstore.as_retriever()