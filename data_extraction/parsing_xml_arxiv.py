#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET
import json
import os
import sys

if __name__ == '__main__':
    # Define the namespace map to handle the namespaces in the XML response
    namespaces = {
        'atom': 'http://www.w3.org/2005/Atom',
        'arxiv': 'http://arxiv.org/schemas/atom'
    }

    base_url = 'http://export.arxiv.org/api/query?'
    search_query = 'cat:cs.AI'  # Sample category
    query = f"search_query={search_query}&start=0&max_results=5"
    response = requests.get(base_url + query)
    root = ET.fromstring(response.content)

    for entry in root.findall('atom:entry', namespaces):
        paper = {
            'id': entry.find('atom:id', namespaces).text,
            'title': entry.find('atom:title', namespaces).text,
            'abstract': entry.find('atom:summary', namespaces).text,
            'published': entry.find('atom:published', namespaces).text[:4],  # Extracting the year
            'authors': [author.find('atom:name', namespaces).text for author in entry.findall('atom:author', namespaces)],
            'primary_category': entry.find('arxiv:primary_category', namespaces).attrib.get('term'),
            'categories': [category.attrib.get('term') for category in entry.findall('atom:category', namespaces)]
        }

        print(json.dumps(paper, indent=2))  # Print the paper for demonstration

    sys.exit()
