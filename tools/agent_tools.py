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
    Create or update a customer lead in Zoho CRM.

    Requires customer name and phone number.
    """

    print("CRM TOOL CALLED - INPUT VALIDATION STARTED")

    # Safely handle None values
    name = (name or "").strip()
    phone = (phone or "").strip()
    city = (city or "").strip()
    product_interest = (product_interest or "").strip()

    if not name:
        return "Customer name not provided. CRM lead not created."

    if not phone:
        return "Customer phone number not provided. CRM lead not created."

    try:
        result = create_or_update_lead(
            name,
            phone,
            city,
            product_interest
        )

        print("CRM LEAD OPERATION COMPLETED")

        return str(result)

    except Exception as e:
        print("CRM LEAD OPERATION FAILED:", type(e).__name__)
        return "Unable to save the customer enquiry due to a technical issue. Please try again later."
