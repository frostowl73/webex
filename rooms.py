import requests

url = "https://webexapis.com/v1/rooms"

payload={}
headers = {
  'Authorization': 'Bearer Yzk0Yzg0MmYtMzQ5Yi00OTBiLWJhZDEtZjk3MDVhNTNmNzUxMDU0YjIzNWYtNTEx_P0A1_54dad50f-fd79-4540-b704-b94600f4f19e'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
