import requests
from config import GROQ_API_BASE, GROQ_API_KEY, GROQ_MODEL_ID

class DeepSeekAgent:
    def __init__(self):
        self.api_base = GROQ_API_BASE
        self.api_key = GROQ_API_KEY
        self.model_id = GROQ_MODEL_ID

    def get_summary(self, text):
        url = f"{self.api_base}/v1/engines/{self.model_id}/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": f"Summarize this data in simple words:\n{text}",
            "max_tokens": 150,
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("text", "")
        return ""
