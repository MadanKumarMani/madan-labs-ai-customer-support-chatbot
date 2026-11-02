import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from tools.rag_tool import search_products


load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)



def customer_chat(question):


    docs = search_products(
        question
    )


    context = ""

    for doc in docs:

        context += doc.page_content



    prompt = f"""

    You are Madan Labs AI Assistant.

    You answer questions about our products.

    Use the below company information:


    {context}



    Customer Question:

    {question}



    Rules:

    - Answer only using company information
    - Be professional
    - Suggest suitable equipment

    """



    response = llm.invoke(
        prompt
    )


    return response.content