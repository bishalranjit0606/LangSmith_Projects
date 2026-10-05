import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

import os 

os.environ['LANGCHAIN_PROJECT'] = 'rag chatbot v1'

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

PDF_PATH = "islr.pdf"

# Load PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

print(f"Total pages: {len(docs)}")

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

splits = splitter.split_documents(docs)

print(f"Total chunks: {len(splits)}")

# Create embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector store
vectorstore = FAISS.from_documents(
    splits,
    embedding
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# Create LLM
llm = ChatOpenAI(
    model="openrouter/free",
    temperature=0.3,
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Answer only from the provided PDF context. "
        "If the answer is not found, say I don't know."
    ),
    (
        "human",
        "Question: {question}\n\nContext:\n{context}"
    )
])

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Build chain
parallel = RunnableParallel(
    context=retriever | RunnableLambda(format_docs),
    question=RunnablePassthrough()
)

chain = (
    parallel
    | prompt
    | llm
    | StrOutputParser()
)

print("PDF RAG ready.")

while True:
    question = input("\nQ: ").strip()

    if question.lower() in ["exit", "quit"]:
        break

    if not question:
        continue

    answer = chain.invoke(question)

    print("\nA:", answer)