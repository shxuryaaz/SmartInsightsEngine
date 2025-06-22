# ingest_sample_data.py

import chromadb

# Use the default in-memory Chroma client (or configure with your server)
client = chromadb.HttpClient(host="localhost", port=8000)  # default Chroma server

# Create or get collection
collection = client.get_or_create_collection(name="support_tickets")

# Sample support tickets
documents = [
    "I'm unable to reset my password even though I followed the instructions.",
    "The reset email is not arriving in my inbox.",
    "My payment method was declined during checkout.",
    "The app crashes every time I try to open it on Android.",
    "I’m getting a 403 error when I try to access the dashboard.",
    "How do I change my account email address?",
    "Can I get a refund for a duplicate charge?",
    "I forgot my password and can’t access my account.",
    "Email verification is failing even after clicking the link.",
    "Notifications aren't working after the latest update."
]

metadatas = [{"source": "sample"} for _ in documents]
ids = [f"ticket_{i}" for i in range(len(documents))]

# Add to vector database
collection.add(documents=documents, metadatas=metadatas, ids=ids)

print("✅ Sample support tickets have been successfully added.")
