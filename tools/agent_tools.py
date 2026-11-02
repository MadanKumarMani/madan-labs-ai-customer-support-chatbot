from langchain_core.tools import tool

from tools.rag_tool import search_products



from agents.customer_agent import customer_chat


from tools.crm_tool import create_or_update_lead

from typing import Optional





@tool
def product_search_tool(question: str):
    """
    Search the Madan Labs knowledge base and return
    relevant product information.
    """

    print("PRODUCT TOOL CALLED")

    docs = search_products(question)

    if not docs:
        return "No relevant products found."

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context





@tool
def crm_lead_tool(
    name: Optional[str] = "",
    phone: Optional[str] = "",
    city: Optional[str] = "",
    product_interest: Optional[str] = ""
):
    """
   Create or update customer lead in Zoho CRM.

    Only use AFTER the customer voluntarily shares
    their contact details.

    Minimum required:
    - customer name
    - phone number

    Optional:
    - city
    - product interest
    """


    print(
        "CRM TOOL CALLED"
    )


    # Don't create/update a CRM record if phone is missing
    if not name.strip():
        return "Customer name not provided. CRM lead not created."

    if not phone.strip():
        return "Customer phone number not provided. CRM lead not created."


    return create_or_update_lead(

        name,

        phone,

        city,

        product_interest

    
    )

