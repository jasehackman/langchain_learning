from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

tool_names = ["wikipedia", "serpapi", "llm-math"]
tools = load_tools(tool_names, llm=llm)

memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
        tools, 
        llm=llm, 
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, 
        verbose=True,
        memory=memory
    )

chat_history = []

try:
    while True:
        query = input("Query: ")
        print(agent.run({"input": query, "chat_history": chat_history}))
except KeyboardInterrupt:
    print("Goodbye!")
