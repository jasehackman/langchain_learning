from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=ConversationBufferMemory()
)

print(conversation.predict(input="Hi there!"))
print(conversation.predict(input="I'm doing well! Just having a conversation with an AI."))
print(conversation.predict(input="Tell me about yourself."))