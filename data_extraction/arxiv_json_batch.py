#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET
import json
import os
import sys

if __name__ == '__main__':

    base_url = 'http://export.arxiv.org/api/query?'
    categories = ['cs.AI', 'cs.CL', 'cs.CV', 'cs.LG', 'cs.MA', 'cs.NE', 'cs.RO', 'stat.ML']
    category_query = ' OR '.join(f'cat:{cat}' for cat in categories)

    start = 0
    max_results = 100
    total_results = float('inf')
    batch_number = 1

    while start < total_results:
        query = f"search_query={category_query}&start={start}&max_results={max_results}"
        response = requests.get(base_url + query)
        root = ET.fromstring(response.content)

        if start == 0:
            total_results_element = root.find('{http://a9.com/-/spec/opensearch/1.1/}totalResults')
            if total_results_element is not None:
                total_results = int(total_results_element.text)

        papers = []
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            paper = {
                'id': entry.find('{http://www.w3.org/2005/Atom}id').text,
                'title': entry.find('{http://www.w3.org/2005/Atom}title').text,
                'abstract': entry.find('{http://www.w3.org/2005/Atom}summary').text,
                'published': entry.find('{http://www.w3.org/2005/Atom}published').text[:10],  # Extracting the full date
                'authors': [author.find('{http://www.w3.org/2005/Atom}name').text for author in
                            entry.findall('{http://www.w3.org/2005/Atom}author')],
                'categories': [category.text for category in entry.findall('{http://www.w3.org/2005/Atom}category')]
            }
            papers.append(paper)

        # Define the directory for storing files
        directory = 'arxiv_data'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Write data to a JSON file
        with open(f'{directory}/papers_batch_{batch_number}.json', 'w') as f:
            json.dump(papers, f, indent=4)

        print(f"Batch {batch_number} saved.")
        batch_number += 1
        start += max_results

    sys.exit()
