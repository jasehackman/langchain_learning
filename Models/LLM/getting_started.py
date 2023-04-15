from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

print(llm("Tell me a joke."))

llm_result = llm.generate(["Tell me a joke.", "Tell me a poem."]*15)
print(len(llm_result.generations))

# get the first generation
print(llm_result.generations[0])

# get the last generation
print(llm_result.generations[-1])

# output provider specific info
print(llm_result.llm_output)

# estimate the number of tokens used
print(llm.get_num_tokens("waht a joke"))