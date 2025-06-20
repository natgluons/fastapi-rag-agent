# import openai
import requests
import os

# Use OpenRouter for local testing
API_KEY = os.environ.get("OPENROUTER_API_KEY")  # or OPENAI_API_KEY if using OpenAI
API_URL = "https://openrouter.ai/api/v1/chat/completions"  # change to OpenAI if needed
MODEL = "google/gemini-2.0-flash-exp:free"  # e.g. "gpt-4o" for OpenAI

# Example config for OpenAI (if you switch over later)
# API_KEY = os.environ.get("OPENAI_API_KEY")
# API_URL = "https://api.openai.com/v1/chat/completions"
# MODEL = "gpt-4o"

def generate_answer(query, retrieved_docs):
    context_text = "\n\n".join(
        [f"[Source: {doc_id}]\n{text}" for doc_id, text in retrieved_docs]
    )

    prompt = f"""
You are an expert AI assistant.

Only use the following context to answer the query below. Do not make up facts.

Context:
{context_text}

Query:
{query}

Answer in a concise, bullet-point format with citations referring to the sources.
""".strip()

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 300
    }

    response = requests.post(API_URL, headers=headers, json=json_data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
