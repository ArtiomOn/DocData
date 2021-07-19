import requests

url = "https://docs.google.com/spreadsheets/d/1UVVP4o3e-6wOl4ucP9lPOQQqPoeQWesxlPmb1lK7Qyk/gviz/tq?tqx=out:csv&sheet=0"

r = requests.get(url)
url_content = r.content

csv_file = open('csv/downloaded.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
