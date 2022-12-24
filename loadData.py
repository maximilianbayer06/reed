import webScraper

data = webScraper.News()

import json
with open('results.json', 'w') as fp:
    json.dump(data, fp)