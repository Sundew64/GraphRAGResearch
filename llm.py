from dotenv import load_dotenv
from openai import OpenAI
from spacy_test import triples_list

load_dotenv()

client = OpenAI()

system_prompt = "Use the triples provided here: " + str(triples_list) + " to answer the question. Do not use any additional information."

prompt = input("what is your question?")

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions = system_prompt,
    input = prompt
)

print(response.output_text)
