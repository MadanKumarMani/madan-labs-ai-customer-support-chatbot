import requests


CLIENT_ID = "PASTE_YOUR_CLIENT_ID_HERE"

CLIENT_SECRET = "PASTE_YOUR_CLIENT_SECRET_HERE"

AUTHORIZATION_CODE = "PASTE_CODE_FROM_BROWSER_HERE"



url = "https://accounts.zoho.in/oauth/v2/token"


params = {

    "grant_type": "authorization_code",

    "client_id": "1000.2JJBYYQ7DGP95SXLVNLSXHTS2IQSXF",

    "client_secret": "e242cfff0f9b26947004bb5fb3f1400b118b8979d2",

    "code": "1000.901e4d605ac52b9c4f3ef99c88b1e385.7428350b9d582d39aa782e46a3ceff0e",

    "redirect_uri": "http://localhost:8501/callback"

}


response = requests.post(
    url,
    params=params
)


print("Zoho OAuth token request completed.")
print("HTTP Status:", response.status_code)
