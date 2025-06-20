# Project structure

* main.py: FastAPI app
* retriever.py: Vector store + retrieval logic
* llm_agent.py: LLM prompt + response handling
* data/: Folder with sample documents
* README.md: How to run (locally or via Docker)

# I tested this on virtual environment locally on windows, so the setup is:

> git clone repo-url
> cd repo-folder
> python -m venv venv
> venv\Scripts\activate # or source venv/bin/activate if you're on Linux or macOS
> pip install -r requirements.txt

create .env file to set openai_api_key
> uvicorn main:app --reload # starting the FastAPI server

# and then I tested the API through POST request via curl in command line
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query":"What are the top 3 use cases for GraphQL in enterprise SaaS?"}'

# that's all, thanks