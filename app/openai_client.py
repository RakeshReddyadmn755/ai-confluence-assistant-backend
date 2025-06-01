from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str):
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an SRE Assistant. Format the input into:\n- What\n- So What\n- Now What\n- Owner\n- Due Date"},
            {"role": "user", "content": text}
        ]
    )
    return chat_completion.choices[0].message.content

