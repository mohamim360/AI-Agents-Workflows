import os  

from openai import OpenAI
from dotenv import load_dotenv  

load_dotenv()  

client = OpenAI()  # Initialize OpenAI client

def generate_x_post(topic: str) -> str:
    # Call AI / LLM to generate a post based on user input
    prompt = f"""
    You are an expert social media manager. Generate a concise and engaging post for X (formerly Twitter).

    Your task is to create a post that is concise, engaging, and suitable for X. The post should be no longer than 280 characters.

    keep the tone professional and informative, while also being engaging and suitable for a wide audience.

    Here's the topic provided by the user:
    <topic>
    {topic}
    </topic>
    """
    resopnse =client.responses.create(
        model="gpt-4o",
        prompt=prompt,
    )

    return respose.output_test
    

def main():
    # User input => AI (LLM) generates X post => Output post
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post:")
    print(x_post)

if __name__ == "__main__":
    main()
