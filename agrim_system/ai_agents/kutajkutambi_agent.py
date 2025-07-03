"""
Kutajkutambi AI Agent
An LLM-based AI agent specialized in agriculture information.
Uses OpenAI GPT or similar LLM to learn and provide agriculture-related knowledge.
"""

import openai

class KutajkutambiAgent:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.system_prompt = (
            "You are Kutajkutambi, an AI agent specialized in agriculture. "
            "Provide accurate, concise, and helpful information about crops, weather, soil, irrigation, pests, and farming best practices."
        )

    def ask(self, user_query: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_query}
            ],
            max_tokens=500,
            temperature=0.7,
            n=1,
            stop=None,
        )
        answer = response.choices[0].message['content'].strip()
        return answer

if __name__ == "__main__":
    import os
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set the OPENAI_API_KEY environment variable.")
        exit(1)

    agent = KutajkutambiAgent(api_key)
    print("Welcome to Kutajkutambi AI Agent. Ask your agriculture questions.")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = agent.ask(query)
        print(f"Kutajkutambi: {answer}\n")
