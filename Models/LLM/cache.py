import time
from langchain.llms import OpenAI

# In Memory Cache
import langchain
from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache()

llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

start_time = time.time()
print(llm("Tell me a joke."))
end_time = time.time()
print("Time to generate: ", end_time - start_time)

start_time = time.time()
print(llm("Tell me a joke."))
end_time = time.time()
print("Time to generate: ", end_time - start_time)