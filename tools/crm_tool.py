import requests
import os
from dotenv import load_dotenv


load_dotenv()


# ================= ACCESS TOKEN =================


def get_access_token():


    url = "https://accounts.zoho.in/oauth/v2/token"


    params = {

        "refresh_token":
        os.getenv("ZOHO_REFRESH_TOKEN"),

        "client_id":
        os.getenv("ZOHO_CLIENT_ID"),

        "client_secret":
        os.getenv("ZOHO_CLIENT_SECRET"),

        "grant_type":
        "refresh_token"
    }


    response = requests.post(
        url,
        params=params
    )


    return response.json()["access_token"]




# ================= CREATE LEAD =================


def create_lead(
    name,
    phone,
    city,
    product
):


    token = get_access_token()


    url = "https://www.zohoapis.in/crm/v7/Leads"


    headers = {

        "Authorization":
        f"Zoho-oauthtoken {token}"
    }


    data = {

        "data":[

            {

                "Last_Name":
                name,

                "Company":
                "AquaAI Chat Customer",

                "Phone":
                phone,

                "City":
                city,

                "Description":
                f"Interested in {product}",

                "Lead_Source":
                "AI Assistant"

            }

        ]

    }


    response = requests.post(
        url,
        headers=headers,
        json=data
    )


    return response.json()





# ================= SEARCH EXISTING LEAD =================


# ================= SEARCH EXISTING LEAD =================


def search_lead(phone):


    token = get_access_token()


    url = "https://www.zohoapis.in/crm/v7/Leads/search"


    headers = {

        "Authorization":
        f"Zoho-oauthtoken {token}"
    }


    params = {

        "criteria":
        f"(Phone:equals:{phone})"
    }


    response = requests.get(

        url,
        headers=headers,
        params=params
    )


    print(
        "SEARCH STATUS:",
        response.status_code
    )


    print(
        "SEARCH RESPONSE:",
        response.text
    )


    try:

        return response.json()


    except Exception:


        return {}




# ================= UPDATE EXISTING LEAD =================


def update_lead(
    lead_id,
    name,
    phone,
    city,
    product
):


    token = get_access_token()


    url = (
        "https://www.zohoapis.in/crm/v7/Leads/"
        + lead_id
    )


    headers = {

        "Authorization":
        f"Zoho-oauthtoken {token}"
    }


    data = {

        "data":[

            {

                "Last_Name":
                name,

                "Phone":
                phone,

                "City":
                city,

                "Description":
                f"Interested in {product}"

            }

        ]

    }



    response = requests.put(
        url,
        headers=headers,
        json=data
    )


    return response.json()





# ================= CREATE OR UPDATE =================


def create_or_update_lead(
    name,
    phone,
    city,
    product
):


    existing = search_lead(phone)


    print(
        "CRM SEARCH:",
        existing
    )


    if (
        existing
        and
        "data" in existing
    ):


        lead_id = existing["data"][0]["id"]


        print(
            "Updating lead:",
            lead_id
        )


        return update_lead(
            lead_id,
            name,
            phone,
            city,
            product
        )


    else:


        print(
            "Creating new lead"
        )


        return create_lead(
            name,
            phone,
            city,
            product
        )