import csv
import json

import requests

from secrets import *

url = f"https://docs.google.com/spreadsheets/d/{KEY}/gviz/tq?tqx=out:csv&sheet={SHEET}"

r = requests.get(url)
url_content = r.content

csv_file = open('data.csv', 'wb')
csv_file.write(url_content)
result = {}
match = {}
words = ["zero", "one", "two", "few", "many", "other"]
with open('data.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if str(row['KEY']).split('__')[-1] in words:
            match = {str(row['KEY']).split('__')[1]: str(row['en'])}
            result[str(row['KEY'])] = match
        else:
            result[row['KEY']] = row['en']

with open('data.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(result, indent=0))

csv_file.close()