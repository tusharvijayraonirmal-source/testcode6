from fastapi import FastAPI
import httpx
import os

app = FastAPI()

LLM_API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv("LLM_API_KEY")


@app.post("/chat")
async def chat(message: str):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a friendly AI character."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            LLM_API_URL,
            json=payload,
            headers=headers,
            timeout=30
        )

    response.raise_for_status()

    data = response.json()
def a():
    
    return {
        "response": data["choices"][0]["message"]["content"]
    }
