# ----------------------------------------------------------------------------
# Trakt OAuth2.0 Authentication Script
#
# This script allows you to authenticate a user with the Trakt API using the 
# OAuth 2.0 flow. It generates an Access Token and Refresh Token that can be
# used to interact with the Trakt API on behalf of the user.
#
# Copyright (c) 2025 suuhm. All Rights Reserved.
#
# Licensed under the MIT License (https://opensource.org/licenses/MIT)
# ----------------------------------------------------------------------------

import requests

def get_trakt_oauth_token(client_id, client_secret, redirect_uri):
    """
    This function uses OAuth2.0 to authenticate the user and fetch an access token.

    :param client_id: Trakt API Client ID
    :param client_secret: Trakt API Client Secret
    :param redirect_uri: Redirect URI for OAuth
    :return: Access Token and Refresh Token
    """
    # Step 1: Generate the authorization URL
    auth_url = f'https://trakt.tv/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}'
    print(f'Please open the following URL in your browser and authorize the app:\n{auth_url}')
    
    # Step 2: Get the authorization code from user
    auth_code = input('Enter the authorization code received: ')
    
    # Step 3: Request Access Token using the authorization code
    token_url = 'https://api.trakt.tv/oauth/token'
    token_data = {
        'code': auth_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    response = requests.post(token_url, data=token_data)
    token_info = response.json()
    
    if 'access_token' in token_info:
        access_token = token_info['access_token']
        refresh_token = token_info['refresh_token']
        print('Access Token received!')
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")
        return access_token, refresh_token
    else:
        print('Error fetching access token:', token_info)
        return None, None

# Example Usage
if __name__ == "__main__":
    # Replace with your Trakt Client ID and Client Secret
    CLIENT_ID = 'YOUR_CLIENT_ID'
    CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    access_token, refresh_token = get_trakt_oauth_token(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

    if access_token:
        print("OAuth Authentication was successful!")
    else:
        print("OAuth Authentication failed.")
