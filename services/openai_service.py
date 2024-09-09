import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize OpenAI API key from environment variable

def ask_openai(question):
    """Call the OpenAI Chat API with a user's question and return the response."""
    try:
        response = client.chat.completions.create(model="gpt-4.",
        messages=[
            {"role": "system", "content": "You are an long standing member of the solutions architecture team at OpenAI. You are a great teacher and coach and want to help those who ask you questions and provide them great answers which are concise and easy to understand."},
            {"role": "user", "content": question}
        ],
        max_tokens=4000)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"
