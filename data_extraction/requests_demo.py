#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import os

if __name__ == '__main__':

    '''
    Hello World with Requests - Making a simple GET request:
    Use the requests library to make a simple GET request to a public API like httpbin (https://httpbin.org/get) and 
    print the response text.
    '''

    response = requests.get('https://httpbin.org/get')
    print(response.text)

    '''
    Parsing JSON from API:
    Make a request to a JSON placeholder service (https://jsonplaceholder.typicode.com/posts/1) and parse the JSON 
    to access specific data fields.
    '''

    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    json_data = response.json()
    print(json_data['title'])  # Accessing the title field from the JSON

    '''
    Using APIs with Authentication:
    Many APIs require authentication. Practice using the requests library to authenticate with an API. You can use 
    APIs like GitHub's API (Note: Ensure you handle your credentials securely).
    '''

    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/user/repos', headers=headers)
    print(response.json())

    sys.exit()
