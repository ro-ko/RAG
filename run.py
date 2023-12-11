# %%
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chains import ConversationChain

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(api_key=api_key, streaming=True,callbacks=[StreamingStdOutCallbackHandler()] , model="gpt-3.5-turbo-1106")

tools  = load_tools(["wikipedia"], llm=chat_model)
# agent = initialize_agent(agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, llm=chat_model, tools=tools, verbose=True)

conversation = ConversationChain(llm=chat_model ,verbose=True)

answer = conversation.predict(input="현재 대한민국의 대통령은 누구인가요?")
print(answer)
# answer = conversation.predict(input="현재 나이가 어떻게 되나요?")
# answer =  chat_model.predict("1박2일은 무슨 프로그램인가요?")

print(conversation.memory)
# %%
