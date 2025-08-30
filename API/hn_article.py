
import requests
import json

# Make a call via API and save the response
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Analyse the data structure
response_dict = r.json()
readable_file = 'API/hn_article.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
    