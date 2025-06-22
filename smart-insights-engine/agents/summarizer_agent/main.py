from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Allow frontend to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set in .env file")

client = OpenAI(api_key=api_key)

@app.post("/summarize")
async def summarize(request: Request):
    try:
        body = await request.json()
        ticket_text = body.get("text", "").strip()

        if not ticket_text:
            raise HTTPException(status_code=400, detail="Missing 'text' in request.")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a helpful support assistant. Summarize the issue briefly."},
                {"role": "user", "content": ticket_text}
            ]
        )

        summary = response.choices[0].message.content.strip()
        return {"summary": summary}

    except Exception as e:
        # Log full error in terminal for debugging
        print("Error while summarizing:", str(e))
        return {"summary": "", "error": str(e)}
