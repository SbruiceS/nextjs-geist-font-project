"""
Kutajkutambi AI Agent using open-source LLM models.
This implementation uses Hugging Face transformers and a local LLM model for agriculture knowledge.
"""

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

class KutajkutambiAgent:
    def __init__(self, model_name="gpt2", device=None):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        if device is None:
            self.device = 0 if torch.cuda.is_available() else -1
        else:
            self.device = device
        self.generator = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer, device=self.device)

        self.system_prompt = (
            "You are Kutajkutambi, an AI agent specialized in agriculture. "
            "Provide accurate, concise, and helpful information about crops, weather, soil, irrigation, pests, and farming best practices."
        )

    def ask(self, user_query: str, max_length=200) -> str:
        prompt = self.system_prompt + "\nUser: " + user_query + "\nAI:"
        outputs = self.generator(prompt, max_length=max_length, num_return_sequences=1)
        answer = outputs[0]['generated_text'][len(prompt):].strip()
        return answer

if __name__ == "__main__":
    agent = KutajkutambiAgent(model_name="gpt2")
    print("Welcome to Kutajkutambi AI Agent (Open Source). Ask your agriculture questions.")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = agent.ask(query)
        print(f"Kutajkutambi: {answer}\n")
