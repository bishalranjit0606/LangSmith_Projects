# LangSmith_Projects

LangSmith lesson scripts: a simple LLM call, a sequential chain, PDF RAG, an agent, and a LangGraph essay evaluator.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy your keys into a local `.env` file. Do not commit that file.

```
GROQ_API_KEY=
OPENAI_API_KEY=
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=
WEATHERSTACK_API_KEY=
```

## Run

```bash
python 1_simple_llm_call.py
python 2_sequential_chain.py
python 3_rag_v1.py
python 3_rag_v2.py
python 3_rag_v4.py
python 4_agent.py
python 5_langgraph.py
```
