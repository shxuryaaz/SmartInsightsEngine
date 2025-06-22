from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from shared.memory.chroma_store import query_memory

app = FastAPI()

# ✅ Allow cross-origin requests from your frontend (important for dashboard.html)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify frontend origin instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/search")
async def search(request: Request):
    try:
        data = await request.json()
        query = data.get("query")

        if not query:
            raise HTTPException(status_code=400, detail="Missing 'query' in request.")

        results = query_memory(query)

        return {"results": results or []}

    except Exception as e:
        return {"error": f"Search failed: {str(e)}"}
