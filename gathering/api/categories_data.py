import requests
from base64 import urlsafe_b64encode
import json
import pandas as pd

df = pd.read_csv("../../temper.csv")

key = "*********"
secret_key = "*********"
list_data = []

for i in df[df['homepage_url'].notnull()]['homepage_url']:
    target_website = bytes(i, encoding='utf-8')
    print('parsing '+target_website.decode('utf-8'))
    try:
        api_url = "https://api.webshrinker.com/categories/v3/%s" % urlsafe_b64encode(target_website).decode('utf-8')
        response = requests.get(api_url, auth=(key, secret_key))
        status_code = response.status_code
        data = response.json()
        if status_code == 200:
            # Do something with the JSON response
            category_data = data['data'][0]['categories']
            # Build a string array containing the category ID, the human friendly category name, score and confident values for each entry
            categories = []
            for entry in category_data:
                categories.append(entry['label'])
            print("'%s' belongs to the following categories:\n%s" % (target_website.decode('utf-8'), "\n".join(categories)))
        elif status_code == 202:
             # The request is being categorized right now in real time, check again for an updated answer
            print("The categories for '%s' are being determined, check again in a few seconds" % target_website)
        else:
            # The different status codes are covered in the documentation (https://docs.webshrinker.com/v3/website-category-api.html)
            print("An error occurred: HTTP %d" % status_code)
            if 'error' in data:
                print(data['error']['message'])
        list_data.append({'homepage_url': target_website.decode('utf-8'), 'categories': categories})
    except:
        print("An error occurred: HTTP %s" % target_website.decode('utf-8'))
        pass

print(list_data)

with open('../../data/url_categories.json', 'w') as fout:
    json.dump(list_data, fout)
print('done')