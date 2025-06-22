from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load trained model and vectorizer
model = joblib.load("model/classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.post("/classify")
async def classify(request: Request):
    data = await request.json()
    text = data.get("text")
    vec = vectorizer.transform([text])
    label = model.predict(vec)
    return {"label": label[0]}
