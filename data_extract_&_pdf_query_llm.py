# -*- coding: utf-8 -*-
"""Copy of Data_Extract_&_PDF_Query_LLM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YDgeeG3buhopz8Y_TrAT2LL_bLekk9Ap
"""

!pip install langchain
!pip install openai
!pip install PyPDF2
!pip install faiss-cpu
!pip install tiktoken

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

# Get your API keys from openai, you will need to create an account.
# Here is the link to get the keys: https://platform.openai.com/account/billing/overview
import os
os.environ["OPENAI_API_KEY"] = " " #put your api key

# connect your Google Drive
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = "/content/gdrive/My Drive/"

# location of the pdf file/files.
reader = PdfReader('/content/gdrive/My Drive/Data/po_order_2.pdf')

reader

# read data from the file and put them into a variable called raw_text
raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

raw_text

raw_text[:100]

# We need to split the text that we read into smaller chunks so that during information retreival we don't hit the token size limits.

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

raw_text

len(texts)

texts[0]

# Download embeddings by HuggingFace
embeddings = HuggingFaceEmbeddings()

docsearch = FAISS.from_texts(texts, embeddings)

docsearch

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "what is the Ship To Address, Date, Material Description, Material Quantity?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)

query = "what is 50"
docs = docsearch.similarity_search(query)
query_embedings= chain.run(input_documents=docs, question=query)
query_embedings



query = "What was the cost of training the GPT4all model?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)

query = "How was the model trained?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)

query = "what was the size of the training dataset?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)

query = "How is this different from other models?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)

query = "What is Google Bard?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)

query = "what trying to make rakesh meena?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)

