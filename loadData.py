import webScraper

data = webScraper.News()

import json
with open('responses.json', 'w') as fp:
    json.dump(data, fp)
