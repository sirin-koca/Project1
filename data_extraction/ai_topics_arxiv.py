#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET
import sys

if __name__ == '__main__':

    '''Extracting all academic papers about AI and ML from the arXiv API involves carefully crafting search 
    query and handling pagination because the API will only return a subset of results per request.
    
    Step 1: Define Search Parameters
    You need to define search queries that target AI and ML topics. The arXiv API allows complex query formation. 
    For AI and ML, you might include terms like "artificial intelligence", "machine learning", "deep learning", etc.'''

    ai_query = ('all:"artificial intelligence" OR '
                'all:"generative artificial intelligence" OR '
                'all:"machine learning" OR '
                'all:"deep learning" OR '
                'all:"neural networks" OR '
                'all:"natural language processing" OR '
                'all:"large language models" OR '
                'all:"GPT4"')

    '''Step 2: Loop Through Paginated Results
    The arXiv API might have a lot of results for your query, and it will paginate them. You need to loop through these
    pages to get all results.
    '''
    base_url = 'http://export.arxiv.org/api/query?'

    # Initialize parameters for pagination
    start = 0
    max_results = 100
    total_results = float('inf')

    while start < total_results:
        query = f"search_query={ai_query}&start={start}&max_results={max_results}"
        response = requests.get(base_url + query)

        # Parse the XML response
        root = ET.fromstring(response.content)

        # Update total_results if it's the first request
        if start == 0:
            total_results_element = root.find('{http://a9.com/-/spec/opensearch/1.1/}totalResults')
            if total_results_element is not None:
                total_results = int(total_results_element.text)

        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            paper_id = entry.find('{http://www.w3.org/2005/Atom}id').text
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            abstract = entry.find('{http://www.w3.org/2005/Atom}summary').text
            published = entry.find('{http://www.w3.org/2005/Atom}published').text[:4]  # Extracting the year

            authors = []
            for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
                name = author.find('{http://www.w3.org/2005/Atom}name').text
                authors.append(name)

            print(
                f"ID: {paper_id}\nTitle: {title}\nYear: {published}\nAuthors: {', '.join(authors)}\nAbstract: {abstract}\n---\n")

        # Prepare for the next batch of results
        start += max_results

    sys.exit()
