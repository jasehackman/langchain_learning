from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="What would be a good company name for a company that makes {product}?",
)

print(prompt.format(product="colorful socks"))