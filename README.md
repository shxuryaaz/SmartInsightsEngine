# Smart Insights Engine

Smart Insights Engine is a lightweight, modular tool built to help customer support teams get more value out of their support tickets. It brings together modern language models, embeddings, and vector search to enable fast search, categorization, and summarization of incoming tickets — all through an intuitive dashboard.

## What It Does

- **Semantic Search**: Find related tickets using vector similarity instead of keywords.
- **Summarization**: Get quick summaries of long ticket messages to save time.
- **Classification**: Automatically tag or categorize tickets based on their content.
- **Modular Backend**: Each feature runs as a separate FastAPI microservice.
- **Persistent Vector Search**: Powered by ChromaDB for storing and querying embeddings.

## Tech Stack

| Component     | Technology                     |
|---------------|--------------------------------|
| Frontend      | HTML, CSS (dark mode), JS      |
| API Services  | FastAPI (Python)               |
| Language Model| OpenAI GPT-3.5 / GPT-4          |
| Embeddings    | LangChain + OpenAI Embeddings  |
| Vector Store  | ChromaDB                       |

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

## How to Run the Project 

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-insights-engine.git
cd smart-insights-engine
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # for Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-openai-api-key
```

## Running the Services

Open separate terminal windows and start each microservice:

```bash
# Start Summarizer
uvicorn agents.summarizer_agent.main:app --port 8001

# Start Classifier
uvicorn agents.classifier_agent.main:app --port 8002

# Start Search Agent
uvicorn agents.search_agent.main:app --port 8003
```

## Load Sample Data for Search

```bash
python ingest_sample_data.py
```

This command adds example support tickets to your ChromaDB collection for semantic search.

## Vector Store Options

**Option 1: Local ChromaDB (default)**

```python
client = chromadb.PersistentClient(path="./chroma")
```

**Option 2: Remote ChromaDB Server**

Start server:

```bash
chroma run --path ./chroma
```

Then connect using:

```python
client = chromadb.HttpClient(host="localhost", port=8000)
```

## Deployment Options

- Frontend (`dashboard.html`) can be hosted on **Netlify**, **Vercel**, or any static host.
- Backend microservices can be deployed via **Render**, **AWS EC2**, **Railway**, or using **Docker** containers.

## Interface Preview

![Dashboard Screenshot](https://i.ibb.co/TxH443ph/Screenshot-2025-06-22-154947.png)

## License

This project is available under the [MIT License](LICENSE).
