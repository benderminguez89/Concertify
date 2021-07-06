import requests
import base64
import datetime

#generates access token for spotify OAUTH
client_id = '935c2db9578b441b8fa287632dd6cc8d'
client_secret = 'c7e68d8cb2ba48c4b464016119b5c66a'

token_url = "https://accounts.spotify.com/api/token"
method = "POST"

token_data = {
    "grant_type": "client_credentials"
}

client_creds = f"{client_id}:{client_secret}"
print(client_creds)
client_creds_b64 = base64.b64encode(client_creds.encode())
print(client_creds_b64)

token_header ={
    "Authorization": f"Basic {client_creds_b64.decode()}" #base64 encoded client_id:client_secret>
}

r = requests.post(token_url, data= token_data, headers= token_header)
print(r.json())
valid_request = r.status_code in range(200, 299)
token_response_data = r.json()

now = datetime.datetime.now()
access_token = token_response_data['access_token']
expires_in = token_response_data['expires_in'] # time in seconds
expires = now + datetime.timedelta(seconds= expires_in)
did_expire = expires < now