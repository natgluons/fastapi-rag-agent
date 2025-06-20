from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retriever import Retriever
from llm_agent import generate_answer

app = FastAPI()
retriever = Retriever()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_endpoint(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    retrieved = retriever.retrieve(request.query, top_k=3)
    sources = [doc_id for doc_id, _ in retrieved]

    answer = generate_answer(request.query, retrieved)

    return {"answer": answer, "sources": sources}
