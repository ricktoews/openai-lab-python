import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_prompt(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    result = completion.choices[0].message

    return result

