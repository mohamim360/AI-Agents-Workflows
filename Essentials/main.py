import os  # Module to access environment variables

import requests  # Library to make HTTP requests to the OpenAI API
from dotenv import load_dotenv  # To load environment variables from .env file

load_dotenv()  # Loads the .env file into your environment

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(usr_input: str) -> str:
    # Call AI / LLM to generate a post based on user input
    payload = {
        "model": "...",  # Replace with actual model like 'gpt-3.5-turbo'
        "input": "...",  # Replace with formatted message input
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    )

def main():
    # User input => AI (LLM) generates X post => Output post
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post:")
    print(x_post)

if __name__ == "__main__":
    main()
