from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.openai_client import summarize_text

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return {"error": "No input text provided"}
    
    try:
        summary = summarize_text(text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}
