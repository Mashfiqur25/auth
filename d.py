import base64
import requests

def get_access_token(client_id, client_secret):
    # Encode client_id and client_secret to base64
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {b64_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info['access_token']
        return access_token
    else:
        print(f"Failed to get access token: {response.status_code}")
        print(response.json())
        return None

if __name__ == "__main__":
    # Replace these with your actual Client ID and Client Secret
    client_id = "c5fe6d9744ea4dcaa2dcca20e6000e33"
    client_secret = "ee3cb7da16c44a58a318e4c1dbeefc04"

    access_token = get_access_token(client_id, client_secret)

    if access_token:
        print(f"Access Token: {access_token}")
    else:
        print("Unable to obtain access token.")
