#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import sys

if __name__ == '__main__':
    # Define input and output file paths
    input_csv_file = 'C:/Users/sirin/OneDrive/Skrivebord/PwrBI/sample-data1-csv.csv'
    output_json_file = 'C:/Users/sirin/OneDrive/Skrivebord/PwrBI/data.json'

    # Convert CSV to JSON
    def csv_to_json(input_csv_file, output_json_file):
        data = []
        with open(input_csv_file, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                # Create a sanitized row with stripped keys
                sanitized_row = {k.strip(): v for k, v in row.items()}
                data.append({
                    "Segment": sanitized_row["Segment"],
                    "Country": sanitized_row["Country"],
                    "AI Topic": sanitized_row["AI Topic"],
                    "Number of employee": int(sanitized_row["Number of employee"]),
                    "Investment $": sanitized_row["Investment $"],
                    "Month Number": int(sanitized_row["Month Number"]),
                    "Month Name": sanitized_row["Month Name"],
                    "Year": int(sanitized_row["Year"])
                })

        # Write the JSON to a file
        with open(output_json_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)


    # Call the function
    csv_to_json(input_csv_file, output_json_file)

    print('CSV data has been written to JSON file successfully.')
    sys.exit()

    sys.exit()
