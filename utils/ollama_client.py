# =========================================================================
# OLLAMA CLIENT: LOCAL REASONING BACKEND (PORT 11434)
# =========================================================================

import requests

class OllamaClient:
    def __init__(self, model="llama3.1"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def run(self, prompt: str):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }
        resp = requests.post(self.url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", "")
