
from fastapi import FastAPI, Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

app = FastAPI()

@app.post("/gmail-fetch")
async def fetch_gmail(request: Request):
    creds = Credentials(token=request.json().get("access_token"))
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    return {"emails": messages[:5]}
