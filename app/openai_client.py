
import os
from openai import OpenAI
from .ingestor import query_collection

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(question):
    docs = query_collection(question)
    context = docs['documents'][0][0] if docs['documents'] else ""
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Use this context: {context}"},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content
