import json
import logging
import requests
from requests.auth import HTTPBasicAuth
import boto3

def handle_api_error(response, path):
    if response.status_code == 400:
        print("According to the API, your request is malformed.")
    elif response.status_code == 401:
        print("Unauthorized error, give the proper credentials.")
        authorized_response = requests.get(path, auth=HTTPBasicAuth(input(), input()))
        return json.loads(authorized_response.text)

    elif response.status_code == 403:
        print("The client attempts a resource interaction that is outside of its permitted scope")
        print("contact with the developers!")
    elif response.status_code == 404:
        print("Client Error: Bad Request for url") 
    elif 500 <= response.status_code < 600:
        print("Sorry, there seems to be an internal issue with the API.")
    else:
        print(f"Got an unexpected status code from the API (`{response.status_code}`).")

# logger = logging.getLogger()

def get_data(response, path):
    if response.status_code == 200:
        data = response.text
        return json.loads(data)
    else:
        return handle_api_error(response, path)

def download_data(path):
    response_api = requests.get(path)
    data = get_data(response_api, path)
    print(data)
    file_name = "E:\\API_VT" + "\\" + "data" + ".json"
    with open(file_name, "w") as file:
        json.dump(data, file)

api = input()  # "https://api.github.com/user/repos"
download_data(api)
