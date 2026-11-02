# AI-Powered Customer Support & Sales Automation Chatbot

An AI-powered chatbot developed using Python, Streamlit, LangChain Agents, Groq AI, and Retrieval-Augmented Generation (RAG) to automate customer support and sales enquiry management.

## Features

- AI-powered customer query handling using Groq LLM.
- RAG-based product information retrieval using ChromaDB.
- LangChain tool-calling agent for selecting appropriate tools.
- Custom product search tool for retrieving relevant product information.
- Zoho CRM API integration for customer lead creation and updates.
- Separate customer and employee interfaces.
- Environment-based configuration for API credentials.

## Architecture

**Overall Workflow:**

Streamlit UI → LangChain Agent → Groq LLM → Tool Selection

**Product Information Retrieval:**

Product Knowledge Base → Embeddings → ChromaDB → Product Search Tool → Retrieved Context → AI Response

**Customer Lead Management:**

Customer Sales Enquiry → CRM Tool → Zoho CRM API → Lead Creation / Update

## Technology Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **LLM:** Groq AI
- **Agent Framework:** LangChain
- **RAG:** Retrieval-Augmented Generation
- **Vector Database:** ChromaDB
- **Embeddings:** Hugging Face Embeddings
- **CRM Integration:** Zoho CRM API
- **API Communication:** REST APIs

## Project Structure

```text
madan_labs_agentic_ai/
│
├── agents/
│   ├── customer_agent.py
│   └── customer_ai_agent.py
│
├── tools/
│   ├── agent_tools.py
│   ├── crm_tool.py
│   └── rag_tool.py
│
├── data/
│   └── products.txt
│
├── app.py
├── create_db.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/MadanKumarMani/madan-labs-ai-customer-support-chatbot.git
cd madan-labs-ai-customer-support-chatbot
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Windows:

```bash
venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Configure environment variables**

Create a `.env` file in the project root and configure the required Groq and Zoho CRM credentials.

Never upload API keys, access tokens, or client secrets to GitHub.

**6. Run the application**

```bash
streamlit run app.py
```

## Future Improvements

- Multi-turn customer lead collection.
- Structured customer information extraction.
- Improved employee dashboard and CRM functionality.
- Conversation memory and lead-state management.

## Author

Madan Kumar Sivasubramani

GitHub: https://github.com/MadanKumarMani
