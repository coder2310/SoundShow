import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"eminem"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "d21c7be6e8msha95dd6ad36f2df0p19216bjsned2b255f715e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)