from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, StorageContext, Settings
import ingestion
import os
import weaviate
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TOKENIZERS_PARALLELISM = os.getenv("TOKENIZERS_PARALLELISM")

#specify embedding model (using huggingface sentence transformer)
embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {"device": "cuda"}
embeddings = HuggingFaceEmbedding(
  model_name=embedding_model_name, 
)
#setting the embedding model
Settings.embed_model = embeddings


#setting up Weaviate vector database
auth_config = weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY"))
client = weaviate.Client(url=os.getenv("WEAVIATE_URL"), auth_client_secret=auth_config)
vector_store = WeaviateVectorStore(weaviate_client=client, index_name="DstackExample")
#setting the vector store as Weaviate
storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

#loading the embedded data into Weaviate specified by the "storage_context"
index = VectorStoreIndex.from_documents(
    ingestion.documents, storage_context=storage_context
)
query_engine = index.as_query_engine()