# Omni Retail AI

Omni Retail AI is an advanced multi-agent system designed to orchestrate complex retail operations. It leverages **Google Gemini 2.0 Flash** to interpret user queries and coordinate four specialized agents to retrieve and process information across shopping, shipping, payments, and customer support domains.

## 🚀 Features

- **Multi-Agent Architecture**:
  - **🛍️ ShopCore**: Manages products, customers, and orders.
  - **🚚 ShipStream**: Tracks shipments and delivery updates.
  - **💳 PayGuard**: Handles wallets, transactions, and balances.
  - **🎧 CareDesk**: Manages customer support tickets and interactions.
- **🤖 AI Orchestrator**: Uses Google Gemini to decompose complex natural language queries into executable steps for specific agents.
- **⚡ High Performance**: Built with **FastAPI** for low-latency responses.
- **🐳 Dockerized**: Production-ready Docker configuration for easy deployment.
- **💻 Frontend UI**: Integrated web interface for interacting with the agents.

## 🛠️ Tech Stack

- **Backend**: Python 3.9, FastAPI, Uvicorn
- **AI/LLM**: Google Generative AI (Gemini 2.0 Flash)
- **Database**: SQLite (managed via SQLAlchemy)
- **Frontend**: HTML5, CSS3, JavaScript
- **Infrastructure**: Docker, Docker Compose

## 📋 Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose
- [Google Cloud API Key](https://aistudio.google.com/) (with access to Gemini models)

## 🏁 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ATripathi13/Omni_retail_ai.git
cd Omni_retail_ai
```

### 2. Environment Configuration
Create a `.env` file in the root directory and add your Google API key:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Run with Docker (Recommended)
Build and run the application container:

```bash
docker-compose up --build
```

The application will be available at:
- **Web UI**: [http://localhost:8000](http://localhost:8000)
- **API Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

### 4. Run Locally (Alternative)
If you prefer running without Docker:

```bash
# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main_api:app --host 0.0.0.0 --port 8000 --reload
```

## 🧪 Testing

To verify the agents are working correctly, you can run the test script:

```bash
python test_agents.py
```

## 📖 API Usage

### Chat Endpoint
**POST** `/api/v1/chat`

Request:
```json
{
  "query": "Check the status of my last order and see if the refund was processed."
}
```

Response:
```json
{
  "query": "...",
  "plan": [ ... ],
  "results": [ ... ],
  "summary": "Your order #101 is delivered. The refund of $50 has been processed successfully."
}
```


