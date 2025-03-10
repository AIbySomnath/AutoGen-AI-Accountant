from agent2 import Agent2

class Agent1:
    def __init__(self):
        self.agent2 = Agent2()

    def process_request(self, user_request):
        raw_data, summary, sql_query = self.agent2.generate_summary(user_request)
        return raw_data, summary, sql_query
