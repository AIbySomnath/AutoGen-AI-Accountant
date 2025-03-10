from smolagents import CodeAgent, OpenAIServerModel
from config import DEEPSEEK_API_BASE, DEEPSEEK_API_KEY, DEEPSEEK_MODEL_ID

class DeepSeekAgent:
    def __init__(self):
        self.model = OpenAIServerModel(
            model_id=DEEPSEEK_MODEL_ID,
            api_base=DEEPSEEK_API_BASE,
            api_key=DEEPSEEK_API_KEY
        )

    def get_summary(self, text):
        prompt = f"Summarize this data in simple words:\n{text}"
        response = self.model.complete(prompt)
        return response if response else "Summary generation failed."