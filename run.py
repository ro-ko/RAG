#%%
from openai import OpenAI
client = OpenAI()

#%%
completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
# %%
print(completion)
# %%
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo-1106")
answer =  chat_model.predict("현재 대한민국의 대통령은 누구인가요?")


# %%
print(answer)
# %%
