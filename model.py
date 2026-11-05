import requests

OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_model(model, system_prompt, user_prompt):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "think": False,
        "options": {"temperature": 0, "seed": 42},
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=600)
    if response.status_code != 200:
        print("Ollama said:", response.text)
    response.raise_for_status()
    return response.json()["message"]["content"]