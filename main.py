import csv
import json
import requests
import os

from datetime import datetime
from secrets import KEY, SHEET

# Create must have directories
os.makedirs('csv', exist_ok=True)
os.makedirs('json', exist_ok=True)

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
        start = datetime.now()
        reader = csv.DictReader(csv_file)
        for row in reader:
            if str(row['KEY']).split('__')[-1] in words:
                match[str(row['KEY']).split('__')[-1]] = str(row[f'{doc_language}'])
                for rand in reader:
                    if str(row['KEY']).split('__')[0] == str(rand['KEY']).split('__')[0]:
                        match[str(rand['KEY']).split('__')[-1]] = str(rand[f'{doc_language}'])
                    else:
                        break
                result[str(row['KEY']).split('__')[0]] = match
                match = {}
                result[rand['KEY']] = rand[f'{doc_language}']
            else:
                match = {}
                result[row['KEY']] = row[f'{doc_language}']

        with open(f'json/{file_name}', 'w', encoding='utf-8', newline='') as jsonFile:
            jsonFile.write(json.dumps(result, indent=0, ensure_ascii=False).replace(r'\\n', r'\n'))

    csv_file.close()
    end_time = datetime.now() - start
    print(f'File {file_name} ended in {end_time}')


key('en', 'data_en.json')
key('ro', 'data_ro.json')
key('po', 'data_po.json')
key('ru', 'data_ru.json')
key('en-us', 'data_en-rus.json')
