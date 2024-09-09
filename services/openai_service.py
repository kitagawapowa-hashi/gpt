import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize OpenAI API key from environment variable

def ask_openai(question):
    """Call the OpenAI Chat API with a user's question and return the response."""
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=100)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"
