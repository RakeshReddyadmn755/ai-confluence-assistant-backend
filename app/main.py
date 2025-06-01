from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .openai_client import summarize_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SREInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: SREInput):
    return {"summary": summarize_text(input.text)}

