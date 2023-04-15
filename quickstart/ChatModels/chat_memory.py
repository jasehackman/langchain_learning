import sys
from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, prompt=prompt, memory=memory)

# print(conversation.predict(input="Hi there!"))
# print(conversation.predict(input="I'm doing well! Just having a conversation with an AI."))
# print(conversation.predict(input="What is your name?"))

print("AI: Hello! How can I help you today?")
while True:
    try:
        user_question= input("You: ")
        print("AI: ", conversation.predict(input=user_question))
    except KeyboardInterrupt:
        sys.exit()