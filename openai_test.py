from openai import OpenAI
from api_pjt.config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)