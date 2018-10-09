import twint
import pandas as pd
import os.path
df = pd.read_csv("../../data/organizations.csv")
for i in df[df['twitter_url'].notnull()]["twitter_url"]:
    user = i.split('/')[-1]
    if os.path.isfile('../../data/twitter-'+ user + '-two.json'):
        print('already-generated')
    else:
        print('needs generating')
        try:
            # Configure
            c = twint.Config()
            c.Username = user
            c.Custom = ["id", "user_id", "username", "timezone","tweet","replies","retweets","likes","date","time","hashtags","mentions","location","link","user_rt"]
            c.Since = '2018-08-01'
            c.Until = '2018-09-01'
            c.Store_json = True
            c.Stats = True
            # Run
            c.Output = "../../data/twitter/twitter-" + user + "-two.json"
            twint.run.Search(c)
        except:
            print('error in: '+  user)
            pass
print('done')
