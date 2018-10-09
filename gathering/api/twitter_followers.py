import tweepy
import os.path
import csv
import json
import pandas as pd

# Keys Hidden for security reasons
consumer_key = '********'
consumer_secret = '********'
access_token = '*******'
access_token_secret = '*********'

# Set up authenticaiton object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up api
api = tweepy.API(auth)
data = []
# Read dataset fro companies
df = pd.read_csv("../../data/organizations.csv")

for i in df["twitter_url"]:
    username = i.split('/')[-1]
    user = api.get_user(username)
    data.append({'username': user.screen_name, 'followers_count': user.followers_count})

print(data)

with open('../../data/twitter_followers.json', 'w') as fout:
    json.dump(data, fout)
print('done')
