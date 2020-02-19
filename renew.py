#v2 02/2020 - adds implementation for refresh token

import webbrowser
import json
import requests
import credentials
import pprint


def main():
    # STEP 1:
    auth_url = 'www.strava.com/oauth/authorize?client_id='+credentials.client_id+'&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all'
    #webbrowser.open('googlechrome://'+auth_url)  # Go to example.com
    print()
    print(auth_url)
    print()
    full_url = input("What is the full URL? ")

    #cut out the url code from the full url for ease
    cut1 = full_url.split('=',2)
    cut2 = cut1[2].split('&',1)
    url_code = cut2[0]

    # STEP 2: (Take code from step one URL and put in "CODE section below" then look for Access Token in response)

    url = 'https://www.strava.com/api/v3/oauth/token'
    data = {
      'client_id': credentials.client_id,
      'client_secret': credentials.client_secret,
      'code': url_code,
      'grant_type': 'authorization_code'
    }

    response = requests.post(url, data=data).json()
    print()
    #pprint.pprint(response)
    print("New Access Token: "+response['access_token'])
    print(response['access_token'],  file=open('./access_token.txt', 'w'))
    print(response['refresh_token'],  file=open('./refresh_token.txt', 'w'))
    #print()
    #print("DONE")

    return response['access_token']

def reauth(refresh_token):
    #accepts prior refresh token to renew the access token

    reauth_url = 'https://www.strava.com/api/v3/oauth/token'
    data = {
    'client_id': credentials.client_id,
    'client_secret': credentials.client_secret,
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
    }
    response = requests.post(reauth_url, data=data).json()
    #print("Response:")
    #pprint.pprint(response)
    print(response['access_token'],  file=open('./access_token.txt', 'w')) #save to file
    print(response['refresh_token'],  file=open('./refresh_token.txt', 'w')) #save to file for next time
    return response['access_token'] #return access token
