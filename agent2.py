from database import execute_query
from deepseek_agent import DeepSeekAgent

class Agent2:
    def __init__(self):
        self.deepseek = DeepSeekAgent()

    def generate_summary(self, user_request):
        sql_query = self.convert_to_sql(user_request)
        raw_data = execute_query(sql_query)
        summary = self.deepseek.get_summary(str(raw_data))
        return raw_data, summary

    def convert_to_sql(self, request_text):
        if "account summary" in request_text.lower():
            return "SELECT account_id, balance, transactions FROM accounts WHERE month = CURRENT_MONTH;"
        return "SELECT * FROM accounts LIMIT 10;"