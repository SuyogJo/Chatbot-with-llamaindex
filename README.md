# Chatbot-with-llamaindex

## Setup

Install the necessary dependencies to run this chatbot. Run the following commands:

```pip install -r requirements.txt```

These are the commands inside requirements.txt:

```
pip install openai
pip install pypdf (if uploaded documents are to be in pdf format)
pip install python-dotenv
pip install torch
pip install sentence-transformers==2.2.2
pip install llama_index
pip install llama-index-vector-stores-weaviate
pip install llama-index-embeddings-huggingface
pip install transformers
```

## How to setup Weaviate vector database

This chatbot uses Weaviate for its backend vector database. To set this up, go to [weaviate.io](weaviate.io) and create a free weaviate account and a weaviate cluster. Note that this free cluster will automatically be deleted after 14 days. Click on "Details" in your cluster and you should copy and paste the cluster URL and API key in a ```.env``` file inside your code folder with the variable names ```WEAVIATE_API_KEY``` and ```WEAVIATE_URL```. 

## How to setup OpenAI API

Go to [```https://openai.com/product```](https://openai.com/product) and create an account. Go to the API Keys section, create an API key and copy paste that to the variable name ```OPENAI_API_KEY``` in ```.env``` file. Then navigate to Settings -> Billing and add at least $1.00 worth of credit.

## Usage Instruction

Upload a document in the ```data``` folder, one which you want to communicate with. After doing all the previous steps, run app.py file in the terminal ```python app.py``` to interact with the document through the chatbot. Enter a prompt when it asks you for one, and the chatbot will respond.

## Modules Details

> ### ingestion.py

This module is for reading and loading the documents uploaded in the "data" folder.

> ### embedding.py

This module is for setting up the embeddings and vector store. For the embedding, we are using "sentence-transformers/all-mpnet-base-v2" from Huggingface.
We also setup the Weaviate vector database. We first setup a Weaviate cluster (more on this below) and we specify the storage context as Weaviate.

> ### app.py

This module is for communicating with the large-language-model. We are using OpenAI's API llm. The user can enter a prompt in the terminal and get an output that ends with "Thank you"

## Replace Embedding Model

If a different embedding model is preferred, install the embedding model from huggingface. Then navigate to ```embedding.py``` and replace the "embedding_model_name" with the one that is preferred.
