import os
import embedding

inp = input("Please enter your prompt: ")

response = embedding.query_engine.query(inp)

print(str(response) + " Thank you.")