#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys

if __name__ == '__main__':
    '''Send a GET Request:
    Use the get method from the requests library to send an HTTP GET request to the JSONPlaceholder API. 
    We'll fetch posts from the /posts endpoint.
    '''
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    '''Check the Status Code:
    Before processing the data, it's a good practice to check the status code of the response. 
    A status code of 200 indicates that the request was successful.'''

    '''Parse the Response Content:
    The data returned by the API is in JSON format. You can parse this data and convert it into a Python object 
    (list of dictionaries in this case) using the json() method.'''
    if response.status_code == 200:
        print('The request was successful.')
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}\nBody: {post['body']}\n---\n")

    else:
        print('Something went wrong, please try again.')

    sys.exit()
