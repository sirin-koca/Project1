#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys

if __name__ == '__main__':
    # Sample query
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = 'cat:cs.AI'  # Sample category
    query = f"search_query={search_query}&start=0&max_results=5"
    response = requests.get(base_url + query)

    # Printing the response content
    print(response.text)

    '''We are looking for the <entry> tags in the XML, as each <entry> represents a paper. 
    Inside each <entry>, we can see the <category> tags. Note how the category information is structured. 
    It's likely to have a format similar to: <category term="cs.AI" scheme="http://arxiv.org/schemas/atom"/>'''

    sys.exit()
