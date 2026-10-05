# day 60 : langsmith 

#  its a observatiuona nd evaulation tool . 

#  why do we need langsmith . 


# senirio no 1
# 
# 
# we work in s a startvup . 
# 
#  sustednt find the the jobb in the recruit nepal . 
#  they look at the jd of the jib ., they modify resume and cover letter. 
# 
#  problem : they havae to do all of this thing manually and multiple times 
# so are making a llm baed application . to solve this probemm .
#  studennt -> upload the jd and the resume -> llm matching the jd and the resume -> cover letter prepeare  and prooff read them ->: cover letter. 
#  we relase this tool and stuidnet loving it . 
# normally the lateny is 2 min , 

#  but one particualr day we finds that many emaila nd peoplemare compaining that that the website is taking mor tan 2 min that is 9, 10 min . 
#  we need to find the rooot cause . 
#  its a compex workflow and we are using multiple lllm the same workflow, like jd match , 

#  ther ear emultoiple stage sand bracnhes and llmm . but we oinly have input and foutpout and the time takwen but we dint have something to lok whuch nide istaking more time or is broken . 

#  the issue might be istead oif scanning the particularc filder in teh google drive we are scaaning the whole folders there . 


# senirio no 2  

# sometimes when we make a workflow to make the caption . 

#  usually it take 20 toke but for some caption caption it takes 100 

# thsi example os of ciast and previous issue was if leatecy 


# 3rd eg :

# we work on  google and 1000 of perople work here as a fresher , 

#  whe npresher joins . they dint know about yje comany ruels , so they sak hr every day , 


#  hr compaine that they have to anser smae asnwer every day . 


#   we make a rag based chatbot so tat user can ask and chatbot can reply . 


#  so tehre is the hullicination in he chatbot . ike 

# a perosn ask ca chatbot what is teh leave policy and chat bot rpely sayaingf there is mno plolicyt leave if you eant 

#  this is m=big mis informatioonm 

#  the rag based system is vsey hard to debug  

#  tany rag based system hullicinate ion two tyoes . 

#  1. fetch the doc wrong doc by the retriver 

# 2. usinf the bad llm , or bad promt or any bad issue with the llm . 

#  oit could be anything. wlike wenn we uodraget the rag we might set the retriver no od doc migt be 1 wjhich is too low liek only 1 . it shiudl have been 3 or 5 like that . 


#  the orimt miughyvt be mistake like in or system message we havet o write if you dint get the cintext just day i dint knwo instea dof making the answe r. you did write that inn  the promt ,. 

#  and debuggungthis in the hukllicination is very very hard. 


#  observibilityv > it is the key term 

# teh commin of 3 eg we have is it is llm based workflow . and the most compext thing abit the llm based is non determistic . 

# trhat for the same input we get the duifferent output . and its very hard to debug this . 

# this oproibelm doesnot leave proper trace 

# observibity helo to know the internal working of any system . end to end treace. 
# and tujhis trace i store d in somewhere which we can uise later 

# langsmith : a tool for abservibiklty cinceot in or system . 

#  comcponent bby compninet 

#  what inout it is taking and what outout it is giving 


# 












#  what does langsmith tarc e ?

# input and putput 
# all the intermiduyate steops. like what retriver sets , what it rerive , etc etc
# latency : time o outout in compoenent level as well
# tokern usage : input na dputput tokens
# cost 
# error 
# tags
# mete data
# feedback 



# eg :

# user -> promt -> llm -> parser -> output

#  thsi sis called proejct in langcmith . 
#  and it will run multiple times 

#  and single execution is called trace in langsmith . 

# and our project have mulktiple component like promtp , llm , parser . 

#  every conmponent that run is caqlled run 

# from nt import environ


# .env

# GROQ_API_KEY=''
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_ENDPOINT='https://api.smith.langchain.com'
# LANGCHAIN_API_KEY=''
# LANGCHAIN_PROJECT='langsmith-demo'

# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# # Simple one-line prompt
# prompt = PromptTemplate.from_template("{question}")

# model = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0
# )
# parser = StrOutputParser()

# # Chain: prompt → model → parser
# chain = prompt | model | parser

# # Run it
# result = chain.invoke({"question": "What is the capital of Nepal?"})
# print(result)

# for sequence chain 

#  for each new project use diiferent project name like 



# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# import os 

# os.environ['LANGCHAIN_PROJECT'] = 'sequential llm app'

# load_dotenv()

# prompt1 = PromptTemplate(
#     template='Generate a detailed report on {topic}',
#     input_variables=['topic']
# )

# prompt2 = PromptTemplate(
#     template='Generate a 5 pointer summary from the following text \n {text}',
#     input_variables=['text']
# )

# model = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0
# )

# parser = StrOutputParser()

# chain = prompt1 | model | parser | prompt2 | model | parser

# config = {
#     "run_name" : "Unemployment in India",
#     "tags" :["llm app", "report generation"],
#     "metadata" : {
#         "topic" : "Unemployment in India",
#         "report_type" : "detailed",
#         "report_length" : "100 words",
#         "report_format" : "markdown",
#         "report_language" : "English",
#     }
# }

# result = chain.invoke({'topic': 'Unemployment in India'}, config=config)

# print(result)


# now eg : 3 
#  check  rag application

#  what is rag applicationin the 2st place 
#  rag iis sucj applicatiomn where we give query _ context . we ask for personal question . 
#  we gove qurery and revelkatent chucnk fomr the dic 

#  the idea is simple i the thery . but in tah pratical is very bad. 

#  the qukITY IS VERY NOT satisfied. 

#  rag can have 2 issue . 

# 1 . retrival iisue . : wrong and irrevalant docs retrived . 
# 2. generator issue : althiugh the retiver fgives good ans ithe llm can hullicinate . 

#  inn prod we cannnot sauy yhat answe is abd becaue of retriver or generator . 

#  we only get the final answer so we dont knwo which is making the issue 

# wec an do this with he help of langsmith 
#   it trace  user wuery , retriverd doc , llm promtpo with insteed doc , llm response 

# import os
# from dotenv import load_dotenv

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
# from langchain_core.output_parsers import StrOutputParser

# import os 

# os.environ['LANGCHAIN_PROJECT'] = 'rag chatbot v1'

# load_dotenv()

# OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENAI_API_KEY not found in .env file")

# PDF_PATH = "islr.pdf"

# # Load PDF
# loader = PyPDFLoader(PDF_PATH)
# docs = loader.load()

# print(f"Total pages: {len(docs)}")

# # Split text
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=150
# )

# splits = splitter.split_documents(docs)

# print(f"Total chunks: {len(splits)}")

# # Create embeddings
# embedding = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # Create vector store
# vectorstore = FAISS.from_documents(
#     splits,
#     embedding
# )

# retriever = vectorstore.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 4}
# )

# # Create LLM
# llm = ChatOpenAI(
#     model="openrouter/free",
#     temperature=0.3,
#     base_url="https://openrouter.ai/api/v1",
#     api_key=OPENROUTER_API_KEY
# )

# # Create prompt
# prompt = ChatPromptTemplate.from_messages([
#     (
#         "system",
#         "Answer only from the provided PDF context. "
#         "If the answer is not found, say I don't know."
#     ),
#     (
#         "human",
#         "Question: {question}\n\nContext:\n{context}"
#     )
# ])

# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# # Build chain
# parallel = RunnableParallel(
#     context=retriever | RunnableLambda(format_docs),
#     question=RunnablePassthrough()
# )

# chain = (
#     parallel
#     | prompt
#     | llm
#     | StrOutputParser()
# )

# print("PDF RAG ready.")

# while True:
#     question = input("\nQ: ").strip()

#     if question.lower() in ["exit", "quit"]:
#         break

#     if not question:
#         continue

#     answer = chain.invoke(question)

#     print("\nA:", answer)

# there is usually 2 issue in here
# langsmith is inly tarcking the  chain but it nit tracking , pdf , load , chunk and endidding is not  track in the langsmith . 
#  langsmioth caqn only trace the runnable in the langchain 
# our entiner rag application id not bering tarced . 

#  thios is prblem no  1 . 

#  2nd isue is logical 
#  the main falw is themore we run this application. we get mor etime to get heanswer . 

#  beaue it s loading the data , chik and ebdding . 

# . than again when we rin it does the same .
# x wehjat should happen is it should have store in teh vectore store 


# sloving woith eg 4 

# for 1st issue : 

# pip install -U langchain langchain-openai langchain-community faiss-cpu pypdf python-dotenv langsmith

# import os
# from dotenv import load_dotenv

# from langsmith import traceable  # <-- key import

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_openai import ChatOpenAI
# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
# from langchain_core.output_parsers import StrOutputParser

# os.environ["LANGCHAIN_PROJECT"] = "rag chatbot v2"

# load_dotenv()

# OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENAI_API_KEY not found in .env file")

# PDF_PATH = "islr.pdf"  # change to your file

# # ---------- traced setup steps ----------
# @traceable(name="load_pdf")
# def load_pdf(path: str):
#     loader = PyPDFLoader(path)
#     return loader.load()  # list[Document]

# @traceable(name="split_documents")
# def split_documents(docs, chunk_size=1000, chunk_overlap=150):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size, chunk_overlap=chunk_overlap
#     )
#     return splitter.split_documents(docs)

# @traceable(name="build_vectorstore")
# def build_vectorstore(splits):
#     emb = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )
#     # FAISS.from_documents internally calls the embedding model:
#     vs = FAISS.from_documents(splits, emb)
#     return vs

# # You can also trace a “setup” umbrella span if you want:
# @traceable(name="setup_pipeline")
# def setup_pipeline(pdf_path: str):
#     docs = load_pdf(pdf_path)
#     splits = split_documents(docs)
#     vs = build_vectorstore(splits)
#     return vs

# # ---------- pipeline ----------
# llm = ChatOpenAI(
#     model="openrouter/free",
#     temperature=0.3,
#     base_url="https://openrouter.ai/api/v1",
#     api_key=OPENROUTER_API_KEY,
# )

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "Answer ONLY from the provided context. If not found, say you don't know."),
#     ("human", "Question: {question}\n\nContext:\n{context}")
# ])

# def format_docs(docs):
#     return "\n\n".join(d.page_content for d in docs)

# # Build the index under traced setup
# vectorstore = setup_pipeline(PDF_PATH)
# retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# parallel = RunnableParallel({
#     "context": retriever | RunnableLambda(format_docs),
#     "question": RunnablePassthrough(),
# })

# chain = parallel | prompt | llm | StrOutputParser()

# # ---------- run a query (also traced) ----------
# print("PDF RAG ready.")

# config = {
#     "run_name": "pdf_rag_query"
# }

# while True:
#     question = input("\nQ: ").strip()

#     if question.lower() in ["exit", "quit"]:
#         break

#     if not question:
#         continue

#     answer = chain.invoke(question, config=config)
#     print("\nA:", answer)

#  here we can treace this function 
# we can use decorator @traceable to trace the function . 

#  @traceable(name="load_pdf")


# but the issue is whith are tarcejd diffrenltuy 
#  what shoudl happen sis rap application shiuld have setuop pipeline nad rag query . 
#  its not currenlty tarcking both in one structiure. its behaviong liek two different tracing
# another brnerfits if @tracabkle is we can add tags like , metadata = {"loader ":"pypdf loader"}

#  imp for each tracable deciratir we can add meta data and tag 



#  now solving teh issue with the latecy 
# pip install -U langchain langchain-openai langchain-community faiss-cpu pypdf python-dotenv langsmith

# import os
# import json
# import hashlib
# from pathlib import Path
# from dotenv import load_dotenv

# from langsmith import traceable

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_openai import ChatOpenAI
# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
# from langchain_core.output_parsers import StrOutputParser

# os.environ["LANGCHAIN_PROJECT"] = "rag chatbot v4"

# load_dotenv()

# OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENAI_API_KEY not found in .env file")

# EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# PDF_PATH = "islr.pdf"  # change to your file
# INDEX_ROOT = Path(".indices")
# INDEX_ROOT.mkdir(exist_ok=True)

# # ----------------- helpers (traced) -----------------
# @traceable(name="load_pdf")
# def load_pdf(path: str):
#     return PyPDFLoader(path).load()  # list[Document]

# @traceable(name="split_documents")
# def split_documents(docs, chunk_size=1000, chunk_overlap=150):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size, chunk_overlap=chunk_overlap
#     )
#     return splitter.split_documents(docs)

# @traceable(name="build_vectorstore")
# def build_vectorstore(splits, embed_model_name: str):
#     emb = HuggingFaceEmbeddings(model_name=embed_model_name)
#     return FAISS.from_documents(splits, emb)

# # ----------------- cache key / fingerprint -----------------
# def _file_fingerprint(path: str) -> dict:
#     p = Path(path)
#     h = hashlib.sha256()
#     with p.open("rb") as f:
#         for chunk in iter(lambda: f.read(1024 * 1024), b""):
#             h.update(chunk)
#     return {"sha256": h.hexdigest(), "size": p.stat().st_size, "mtime": int(p.stat().st_mtime)}

# def _index_key(pdf_path: str, chunk_size: int, chunk_overlap: int, embed_model_name: str) -> str:
#     meta = {
#         "pdf_fingerprint": _file_fingerprint(pdf_path),
#         "chunk_size": chunk_size,
#         "chunk_overlap": chunk_overlap,
#         "embedding_model": embed_model_name,
#         "format": "v1",
#     }
#     return hashlib.sha256(json.dumps(meta, sort_keys=True).encode("utf-8")).hexdigest()

# # ----------------- explicitly traced load/build runs -----------------
# @traceable(name="load_index", tags=["index"])
# def load_index_run(index_dir: Path, embed_model_name: str):
#     emb = HuggingFaceEmbeddings(model_name=embed_model_name)
#     return FAISS.load_local(
#         str(index_dir),
#         emb,
#         allow_dangerous_deserialization=True
#     )

# @traceable(name="build_index", tags=["index"])
# def build_index_run(pdf_path: str, index_dir: Path, chunk_size: int, chunk_overlap: int, embed_model_name: str):
#     docs = load_pdf(pdf_path)  # child
#     splits = split_documents(docs, chunk_size=chunk_size, chunk_overlap=chunk_overlap)  # child
#     vs = build_vectorstore(splits, embed_model_name)  # child
#     index_dir.mkdir(parents=True, exist_ok=True)
#     vs.save_local(str(index_dir))
#     (index_dir / "meta.json").write_text(json.dumps({
#         "pdf_path": os.path.abspath(pdf_path),
#         "chunk_size": chunk_size,
#         "chunk_overlap": chunk_overlap,
#         "embedding_model": embed_model_name,
#     }, indent=2))
#     return vs

# # ----------------- dispatcher (not traced) -----------------
# def load_or_build_index(
#     pdf_path: str,
#     chunk_size: int = 1000,
#     chunk_overlap: int = 150,
#     embed_model_name: str = EMBED_MODEL,
#     force_rebuild: bool = False,
# ):
#     key = _index_key(pdf_path, chunk_size, chunk_overlap, embed_model_name)
#     index_dir = INDEX_ROOT / key
#     cache_hit = index_dir.exists() and not force_rebuild
#     if cache_hit:
#         return load_index_run(index_dir, embed_model_name)
#     else:
#         return build_index_run(pdf_path, index_dir, chunk_size, chunk_overlap, embed_model_name)

# # ----------------- model, prompt, and pipeline -----------------
# llm = ChatOpenAI(
#     model="openrouter/free",
#     temperature=0.3,
#     base_url="https://openrouter.ai/api/v1",
#     api_key=OPENROUTER_API_KEY,
# )

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "Answer ONLY from the provided context. If not found, say you don't know."),
#     ("human", "Question: {question}\n\nContext:\n{context}")
# ])

# def format_docs(docs):
#     return "\n\n".join(d.page_content for d in docs)

# @traceable(name="setup_pipeline", tags=["setup"])
# def setup_pipeline(pdf_path: str, chunk_size=1000, chunk_overlap=150, embed_model_name=EMBED_MODEL, force_rebuild=False):
#     return load_or_build_index(
#         pdf_path=pdf_path,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap,
#         embed_model_name=embed_model_name,
#         force_rebuild=force_rebuild,
#     )

# @traceable(name="pdf_rag_full_run")
# def setup_pipeline_and_query(
#     pdf_path: str,
#     question: str,
#     chunk_size: int = 1000,
#     chunk_overlap: int = 150,
#     embed_model_name: str = EMBED_MODEL,
#     force_rebuild: bool = False,
# ):
#     vectorstore = setup_pipeline(pdf_path, chunk_size, chunk_overlap, embed_model_name, force_rebuild)
#     retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

#     parallel = RunnableParallel({
#         "context": retriever | RunnableLambda(format_docs),
#         "question": RunnablePassthrough(),
#     })
#     chain = parallel | prompt | llm | StrOutputParser()

#     return chain.invoke(
#         question,
#         config={"run_name": "pdf_rag_query", "tags": ["qa"], "metadata": {"k": 4}}
#     )

# # ----------------- CLI -----------------
# if __name__ == "__main__":
#     print("PDF RAG ready.")

#     while True:
#         question = input("\nQ: ").strip()

#         if question.lower() in ["exit", "quit"]:
#             break

#         if not question:
#             continue

#         answer = setup_pipeline_and_query(PDF_PATH, question)
#         print("\nA:", answer)


#  when index changes 

# 1. no cache exists yet means first evr run 
# 2. pdf content changes  like even meta data as well 
# 3. pdf file metqadata for rg size and chunk overlap

# 4. chaunk oarams change -> chunk size or chnk overlao 

# 5. enbedding modle name chsnge 

#  now runnign the agnet cide for tha lkansmith 

# import os
# import requests
# from dotenv import load_dotenv

# from langchain_groq import ChatGroq
# from langchain_core.tools import tool
# from langchain_community.tools import DuckDuckGoSearchRun
# from langchain_classic.agents import create_react_agent, AgentExecutor
# from langsmith import Client

# os.environ["LANGCHAIN_PROJECT"] = "agent"

# load_dotenv()

# if not os.getenv("GROQ_API_KEY"):
#     raise ValueError("GROQ_API_KEY not found in .env file")

# search_tool = DuckDuckGoSearchRun()

# @tool
# def get_weather_data(city: str) -> str:
#   """
#   This function fetches the current weather data for a given city
#   """
#   url = f'https://api.weatherstack.com/current?access_key=YOUR_WEATHERSTACK_API_KEY&query={city}'

#   response = requests.get(url)
#   response.raise_for_status()

#   return str(response.json())

# llm = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0,
# )

# # Step 2: Pull the ReAct prompt from LangChain Hub
# prompt = Client().pull_prompt(
#     "hwchase17/react",
#     dangerously_pull_public_prompt=True,
# )
# prompt.template += (
#     "\nAfter Action Input, stop. Do not write Observation yourself. "
#     "Wait for the tool result, then write Thought and Final Answer.\n"
# )

# # Step 3: Create the ReAct agent manually with the pulled prompt
# agent = create_react_agent(
#     llm=llm,
#     tools=[search_tool, get_weather_data],
#     prompt=prompt
# )

# # Step 4: Wrap it with AgentExecutor
# agent_executor = AgentExecutor(
#     agent=agent,
#     tools=[search_tool, get_weather_data],
#     verbose=True,
#     max_iterations=5,
#     handle_parsing_errors=True,
# )

# # What is the release date of Dhadak 2?
# # What is the current temp of gurgaon
# # Identify the birthplace city of Kalpana Chawla (search) and give its current temperature.

# # Step 5: Invoke
# response = agent_executor.invoke({"input": "What is the current temp of gurgaon"})
# print(response)

# print(response['output'])

#  now we will learn about th elanggrapgh intrgration with the langsmith 

#  langgraogh helps to indentify the the prject as a workflow . 

#  we identify project . 

#  the langgrapogh debug is very hard. 

#  we can stire the whole graopgh exectuion be logged in langsmith as a trace 

# each node eg retriver llm , tool call, sub graogh  become a run indisde the trace 

# you can visualize the path taken. 

# from tkinter import END


# start -> retriver -> ranker -> llm answer -> END

# other fetaire of langsmith 

#  we only learn abiut the ibserviikity 

#  monitoring an aleriting 

#  we can set alert for us . 

#  we cam observe the trace . 

#  we can trace the multiplr traces liek if we see  too many request at once we  remove it 


#  grewtaly uise in oprduction env ,. 


#  if we fuind the latwecy increse ibr the multiple trace thatn its a orobelm . 

#  forr evaulation. llm is no  demetrtoscs in nature. taht menas we get the different answer . 
#  like we get totally differnt answr like change in the prompt or chanbge the llm modle 

# to measue if the previous llm is good or bad . 

#  we try out in stardatise data set. 

#  bets example is llm as a juidge 
#  we canmake evaluator liek pre buil evalautir , we can makle own evualtor , it comes under llm ops . 

#  promt experiment 

#  allwos us to systematically test and comapre different prompt verdsion/ 

#  we can run thr ab test 

#  therse is sectio nof poromt engineering 

#  tyhere is palyground . 


#  data set creratign and annotation . 


#  provide too;l to build dataset for evaualtion and fine tuniing 

# support manual annotataion 
# store data set


# user feedback integration 
#  lets you capture the up and down  , rating  m, structure feedback fom the user ubn orduction

# collaboratioon

#  we can copy teh link of teh trace and share to the team 


