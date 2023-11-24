import json
import requests
import pandas as pd

base = "https://itunes.apple.com/search"
r = requests.get(base, params={"term": "Dawid Podsiadło", "country": "pl", "limit": 2})
r.status_code
print(r.url)
info = r.json()
print(json.dumps(info, indent=4))
songs_df = pd.DataFrame(info["results"])
songs_df.to_excel("songs_info.xlsx")
