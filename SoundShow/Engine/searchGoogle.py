API_KEY = "AIzaSyBwqgxbGm7pwTbe16s3q5l1qlvIwjc3jWA"
CSE = "005285266836429124178:31ep92ksgbo"
from googleapiclient.discovery import build
import json
CREDENTIALS = {
  "type": "service_account",
  "project_id": "soundshow",
  "private_key_id": "59c71872642f10c256b1fb4f961e6b7b44b0ab59",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCiCb1/C5GdGHEY\nNAZVkYC5/FjmlK7PzyZlyQ15TCNperycT8AOJ5SL7EFNJKpPUxq/OQCcGl60Ow7N\nfAxoFQjfxTlD+vsd0Xy7YB/2QsjDczaMalLGdFF3T2WD5gBTqgWplToTSw3LXLIg\nEGdp4ymG8rt7MIa7rcz0s2FPjL8Iulkvg5E19Yl+iGPY3ZfbCEisq2wUWLB6Z6ha\n/BflqEjJi4p7fJOJSYPWaZgqAXiKwVKW1wEfZ86Vfd9y+OM2AzlKLXgVLniQ9hzl\n44SJoRRcztv++oNfKklbF7hD9RrmjmU4uQcapQIGwkDEe811frNAmhnxtjVUh+xc\nauWrKYLTAgMBAAECggEADuOiO/hOKwdB7R1qr5YtI+niKV3kKkg4mQW+bTTn1Btp\nFVvmo+ZTKgBNh88kryFNxeBxA+cQaLM8ivkpEq9MH3O57Vs0k+rZ8UXF6hT86ai+\njGyAqqepjLMI+vO5d/aZipmhuoAdBmDAJV4cgohTGolXXNx6pOg1ew64lFy0eRKx\nB87HckGaYbd2ZPOP2wbiid+5ae7YoLWWg7JvQWbLd1gACCDhU8+ioThrURcORhKf\nlo7vP6k+baOt2KWJyK7u8NfWHKvqCLc2Ncm6VIZeM8iYoABwbIAUm6Msyu4EeCrB\nURs8/ChzButlQBQF+Mp+AGwMEHOKWO9Q+LshmJVZUQKBgQDSnSP6UwevF4nOdBlD\nedkz+BcJNxEGF2HRxYc6ysBX92J/m1YYaiDWWPF5Jzfp8a2phKoSJnRPy+0fQLxY\ncvDMYg6ChWIA1SrqofWFDPlwa2CoCJzcG7937ZnZpOF+JJlm0SeGNM2JE6vHlTla\n+KhtM5T76vuWxUWKpHFRyukC9QKBgQDE9NYkJfdu9sXI0Gf2PFaMo3qnqVIZcaMp\nQVRuEulvKDmQLxi7B0/amabcNGySCS6gbv8zOC+vzqmDj98Vw0vqfjxrzh5QQbwb\nsS9f5ALsNHqDhGREV+LSSjeJ2bUCQ/zsN0Ck4zrluBCZg+MNBbO4nv/+zVsw8lLh\nP8ABDkshpwKBgQCQ9+TpyvkBBhyu5K73CQn+gYepqiOno7SLJYF9cE2QvxEncI6E\nY5iSscoUcHBGMTot8sj1kU6CFoXy+yYpY4Rnyh7erFzW4eOWeUB8AoA3Z1Gyl6sQ\nvnC+Zed+LcWghCSq5tBjyjinX8jfqdE+0uVrtROZixb9om/JjIMLn7VfeQKBgQCB\nqAf8nf3IT62eaAu4Xro/NTN+ggmo9FULyJUTLWH8qgdS8p4eKU8ZQgNFfUFn1aGb\nPdbEWh2SZ8LR9/lM81bblKSj93mfLdbuh/L+9jQyWM26HIKBNzX7Z54uImJ1jlpH\nCoyEv427QjOzS85BeVp5lDpD+94nV67V18jHKSiuiwKBgEybukiamLD9m6IIAAuI\nVGu3oqyagmqkVrBtMb14Eru2gRZDKDVkXwuEGBIuX3Vu5yoqh7kTPd/MpvK0uwf5\n6d2G3xnm1jdpY+TXLurDpzg4uSCYUgFDP7JcBPT6/41J/n12FmwLH9qNNaBr1BG9\ng8jw1icLxe4OGbErs7GpSYvi\n-----END PRIVATE KEY-----\n",
  "client_email": "aks646@soundshow.iam.gserviceaccount.com",
  "client_id": "101422654657903657419",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/aks646%40soundshow.iam.gserviceaccount.com"
}

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

def search(term):
  return google_search(term, API_KEY,CSE)

#terms = ["nyc", "corona virus", "jordans 2020"]
def search_list(lst):
  for term in lst:
    yield search(term)
