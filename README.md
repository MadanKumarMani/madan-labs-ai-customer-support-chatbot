# AI-Powered Customer Support & Sales Automation Chatbot

An AI-powered customer support and sales automation chatbot built with Python, Streamlit, LangChain Agents, Groq AI, and Retrieval-Augmented Generation (RAG). The application answers product-related enquiries using a product knowledge base and captures genuine sales enquiries in Zoho CRM.

**Live Demo:** [Open the chatbot](https://madan-ai-labs.duckdns.org/chat/)  
**GitHub:** [View source code](https://github.com/MadanKumarMani/madan-labs-ai-customer-support-chatbot)


## Features

- **AI-powered customer support:** Handles customer product enquiries using a Groq-hosted language model.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant product information from a custom knowledge base using ChromaDB and Hugging Face embeddings.
- **LangChain tool-calling agent:** Selects and invokes the product-search or CRM tool according to the customer enquiry.
- **Product search:** Searches the product knowledge base and supplies relevant context for generated responses.
- **Zoho CRM integration:** Uses Zoho CRM REST APIs to search for existing leads and create or update customer records.
- **Conversational lead capture:** Uses customer-provided details and buying intent to support sales lead capture.
- **Customer and employee views:** Includes separate customer and employee interface options. The employee view currently provides basic login functionality; its CRM assistant response is a placeholder.
- **Cloud deployment:** Hosted on an AWS EC2 Ubuntu instance and exposed through NGINX and a DuckDNS domain.
- **HTTPS security:** Uses a Let's Encrypt SSL/TLS certificate obtained and configured with Certbot.
- **Environment-based configuration:** Keeps API credentials in environment variables rather than hardcoding them in application code.

## Architecture

### Overall workflow

```text
Customer
   |
   v
Streamlit User Interface
   |
   v
LangChain Agent <----> Groq LLM
   |
   +----> Product Search Tool
   |          |
   |          v
   |      ChromaDB
   |          |
   |          v
   |      Retrieved Product Context
   |
   +----> CRM Lead Tool
              |
              v
         Zoho CRM REST API
              |
              v
       Search / Create / Update Lead
```

### RAG product retrieval workflow

```text
Product Knowledge Base (data/products.txt)
                 |
                 v
             Text Splitting
                 |
                 v
       Hugging Face Embeddings
                 |
                 v
              ChromaDB
                 |
                 v
        Product Search Tool
                 |
                 v
       Retrieved Product Context
                 |
                 v
           Groq LLM Response
```

### Customer lead management workflow

```text
Customer Sales Enquiry
          |
          v
    LangChain Agent
          |
          v
    CRM Lead Tool
          |
          v
    Zoho CRM REST API
          |
          v
 Search Existing Lead by Phone
          |
       +--+--+
       |     |
     Found  Not Found
       |     |
       v     v
    Update  Create
       |     |
       +--+--+
          |
          v
     Zoho CRM Lead
```

### Deployment architecture

```text
User Browser (HTTPS)
        |
        v
DuckDNS Domain
        |
        v
NGINX Reverse Proxy
        |
        v
AWS EC2 Ubuntu Instance
        |
        v
Streamlit Application
```

Certbot manages the Let's Encrypt certificate used by NGINX for HTTPS.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / UI | Streamlit |
| LLM | Groq AI |
| Agent Framework | LangChain |
| Retrieval Architecture | Retrieval-Augmented Generation (RAG) |
| Vector Database | ChromaDB |
| Embeddings | Hugging Face Embeddings |
| CRM Integration | Zoho CRM REST API |
| API Communication | REST APIs |
| Cloud Infrastructure | AWS EC2 |
| Operating System | Ubuntu Linux |
| Web Server / Reverse Proxy | NGINX |
| Domain / DNS | DuckDNS |
| SSL/TLS | Let's Encrypt, Certbot |
| Secure Web Access | HTTPS |

## Project Structure

```text
madan-labs-ai-customer-support-chatbot/
|
|-- agents/
|   |-- customer_agent.py
|   `-- customer_ai_agent.py
|
|-- tools/
|   |-- agent_tools.py
|   |-- crm_tool.py
|   `-- rag_tool.py
|
|-- data/
|   `-- products.txt
|
|-- app.py
|-- create_db.py
|-- requirements.txt
|-- .gitignore
`-- README.md
```

The ChromaDB vector database is generated from the product knowledge base using `create_db.py`. The generated database directory is not committed to the repository and should be created during setup.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/MadanKumarMani/madan-labs-ai-customer-support-chatbot.git
cd madan-labs-ai-customer-support-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Ubuntu:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add the required credentials:

```env
GROQ_API_KEY=your_groq_api_key
ZOHO_REFRESH_TOKEN=your_zoho_refresh_token
ZOHO_CLIENT_ID=your_zoho_client_id
ZOHO_CLIENT_SECRET=your_zoho_client_secret
```



### 6. Generate the vector database

```bash
python create_db.py
```

This reads the product knowledge base and creates the ChromaDB vector store used by the product-search tool.

### 7. Run the application

```bash
streamlit run app.py
```

Open the local application at:

```text
http://localhost:8501
```

## AWS Deployment

The application is deployed on an AWS EC2 Ubuntu instance. The deployment setup includes:

- Provisioning an EC2 instance and preparing the Ubuntu environment.
- Installing Python dependencies and configuring a Python virtual environment.
- Configuring Groq AI and Zoho CRM credentials through environment variables.
- Generating the ChromaDB vector store on the server.
- Hosting the Streamlit application on the EC2 instance.
- Configuring NGINX as a reverse proxy for public application access.
- Configuring DuckDNS to point the domain to the EC2 public IP address.
- Installing a Let's Encrypt SSL/TLS certificate using Certbot.
- Configuring HTTPS access through NGINX.

## Security Notes

- Keep `.env` out of Git using `.gitignore`.
- Never expose API keys, Zoho refresh tokens, client secrets, or private SSH keys.
- Restrict SSH access to trusted IP addresses in the EC2 security group.
- Use HTTPS for public access to the application.
- The employee login in the current demo is basic and should be replaced with secure authentication before production use.

## Future Improvements

- Improve multi-turn lead collection and structured customer information validation.
- Implement persistent conversation and lead-state management.
- Build a functional employee CRM assistant and dashboard.
- Improve employee authentication and role-based access control.
- Add automated tests, structured logging, and monitoring.
- Improve error handling and CRM API response validation.

## Author

**Madan Kumar Sivasubramani**

GitHub: [MadanKumarMani](https://github.com/MadanKumarMani)