from langchain import OpenAI

from myapp.langchaindemo import load_openai_api_key

load_openai_api_key()

client=OpenAI()


response=client.generate(model="gpt-3.5-turbo",
  temperature=0.5,
  max_tokens=100,
  prompts=["请给我的花店起个名"])



print(response)