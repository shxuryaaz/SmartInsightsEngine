# Smart Insights Engine

Smart Insights Engine is a modular, AI-powered support dashboard that enables customer support teams to rapidly analyze, classify, and search support tickets using LLMs, embeddings, and vector databases.

## Features

- **Semantic Search**: Search similar support tickets using vector similarity.
- **Summarization**: Generate concise summaries of ticket content.
- **Classification**: Categorize support tickets using intent detection.
- **Modular Architecture**: Each feature is served via independent FastAPI microservices.
- **Vector Store**: Uses ChromaDB for persistent vector search.

## Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Frontend     | HTML, CSS (dark mode), JS      |
| Backend APIs | FastAPI (Python)               |
| LLM          | OpenAI GPT-4 / GPT-3.5         |
| Embeddings   | LangChain + OpenAI Embeddings  |
| Vector Store | ChromaDB                       |

## Project Structure

```
smart-insights-engine/
├── agents/
│   ├── search_agent/
│   ├── summarizer_agent/
│   ├── classifier_agent/
│
├── shared/
│   └── memory/
│       └── chroma_store.py
│
├── dashboard.html
├── ingest_sample_data.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-insights-engine.git
cd smart-insights-engine
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-openai-api-key
```

## Running the Microservices

Use separate terminals to start each agent:

```bash
# Summarization Service
uvicorn agents.summarizer_agent.main:app --port 8001

# Classification Service
uvicorn agents.classifier_agent.main:app --port 8002

# Semantic Search Service
uvicorn agents.search_agent.main:app --port 8003
```

## Ingest Sample Data for Semantic Search

```bash
python ingest_sample_data.py
```

This populates the ChromaDB vector store with embeddings for ticket examples.

## ChromaDB Options

**Option A (default): Local persistent mode**

```python
client = chromadb.PersistentClient(path="./chroma")
```

**Option B: Remote Chroma server**

Start server:

```bash
chroma run --path ./chroma
```

Then use:

```python
client = chromadb.HttpClient(host="localhost", port=8000)
```

## Deployment Options

- **Frontend** (`dashboard.html`) can be deployed on Netlify, Vercel, or any static web host.
- **Backend services** can be deployed to Render, AWS EC2, Railway, or Docker containers.

## Screenshot

![Dashboard Screenshot](https://i.ibb.co/TxH443ph/Screenshot-2025-06-22-154947.png)

## License

This project is licensed under the MIT License.
