import os
import csv
import json
import requests

# Create must have directories
os.mkdir('csv')
os.mkdir('json')

# Docs data
KEY = '1UVVP4o3e-6wOl4ucP9lPOQQqPoeQWesxlPmb1lK7Qyk'
SHEET = 0

# Base docs url
url = f"https://docs.google.com/spreadsheets/d/{KEY}/gviz/tq?tqx=out:csv&sheet={SHEET}"
request = requests.get(url)
url_content = request.content


def key(doc_language, file_name):
    csv_file = open('csv/data.csv', 'wb')
    csv_file.write(url_content)
    words = ["zero", "one", "two", "few", "many", "other"]
    result = {}

    with open('csv/data.csv', encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if str(row['KEY']).split('__')[-1] in words:
                match[str(row['KEY']).split('__')[1]] = str(row[f'{doc_language}'])
                result[str(row['KEY']).split('__')[0]] = match
            else:
                match = {}
                result[row['KEY']] = row[f'{doc_language}']

        with open(f'json/{file_name}', 'w', encoding='utf-8', newline='') as jsonFile:
            jsonFile.write(json.dumps(result, indent=0, ensure_ascii=False))

        csv_file.close()


key('en', 'data_en.json')
key('ro', 'data_ro.json')
key('po', 'data_po.json')
key('ru', 'data_ru.json')
key('en-us', 'data_en-rus.json')
