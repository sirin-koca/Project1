#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET
import sys

if __name__ == '__main__':
    '''Send a GET Request to the arXiv API
    Define the base URL for the arXiv API and set your search parameters. The arXiv API uses a query-based system for 
    fetching results. For simplicity, let's fetch the last 10 submissions.'''
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = 'all:artificial intelligence, machine learning'
    start = 0  # start at the first result
    max_results = 10  # get 10 results

    query = f"search_query={search_query}&start={start}&max_results={max_results}"

    response = requests.get(base_url + query)

    '''Parse the XML Response
    The response from the arXiv API is in XML format. 
    We need to parse this response to extract the needed information.'''
    root = ET.fromstring(response.content)

    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        paper_id = entry.find('{http://www.w3.org/2005/Atom}id').text
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        abstract = entry.find('{http://www.w3.org/2005/Atom}summary').text
        published = entry.find('{http://www.w3.org/2005/Atom}published').text[:10]  # Extracting the date

        # Authors are under the <author> tag
        # Note: Affiliation and country are not directly available; they might be part of the author name in some cases
        authors = []
        for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
            name = author.find('{http://www.w3.org/2005/Atom}name').text
            authors.append(name)

        print(
            f"ID: {paper_id}\nTitle: {title}\nYear: {published}\nAuthors: {', '.join(authors)}\nAbstract: {abstract}"
            f"\n---\n")

    sys.exit()
