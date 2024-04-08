from src.helper import load_data,split_data,download_hugging_face_embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from pinecone import Pinecone
import os

#LOADING API KEYS
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
PINECONE_HOST = os.environ.get('PINECONE_HOST')

#extarct data and split it
extract_data = load_data("data/G.pdf")
text_chucks = split_data(extract_data)



# emedding
embedding = download_hugging_face_embeddings()

#initialization of pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

#index
index_name = "chat-bot"
index = pc.Index(host=PINECONE_HOST)


#push to pinecone
docsearch = PineconeVectorStore.from_documents(text_chucks, embedding, index_name=index_name)