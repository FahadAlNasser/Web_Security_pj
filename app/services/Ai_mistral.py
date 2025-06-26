import requests
import os
from dotenv import load_dotenv

load_dotenv()

Deepinfra_api_key = os.getenv("deepfra_key")

def result_summarizing(question: str, context: str):
    url = "https://api.deepinfra.com/v1/openai/chat/completions"
    headers = {
        "Authorization": f"Bearer {Deepinfra_api_key}",
        "Content-type": "application/json"
    }
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}"
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 200
    }
    response = requests.post(url, headers = headers, json = payload)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    return f"There is an AI error: {response.status_code} - {response.text}"