# Predicting website traffic using twitter account feed



## DATASET Description 

### Dependent variable

```
possible dependent variable: [reach_per_million, page_views_per_million, rank]
```
preferred variable: reach_per_million [the rank is global and all the available data have a low rank]

#### Dictionary:-
* Reach per million value - This metric means "out of a million global internet users, how many visited this site (during the specified time range)?" replaced by views
* Page views per million value - This metric means "out of a million pageviews made by the Alexa traffic panel (during the specified time range), how many were on this site?" Note that the pageviews are not unique.



### Features

#### Dictionary:-

* hashtags: how many hashtags did this account include
* likes: how many likes did this account recieve
* links:  how many links to their website did this account include
* replies:  how many replies did this account recieve
* retweets:  how many retweets did this account recieve
* total_tweets:  how many tweets did this account tweet
* word_count: count of words
*is_weekend: if this date is weekend or not
* links_in_count:	A count of links pointing in to this site (no historic data available only current value)
* followers_count: total followers count

Summary of attributes
We have 6956 observations and 52 features including dummy variables

| Column Name   |      type     |     Description    |
| ------------- | ------------- | -------------------
|   views       | float   | Number of visitors (A visit is defined as an entry to a web domain from a different web domain or from the beginning of an empty browsing session, and expires after 30 minutes of inactivity)
|      date     | date | The date of the traffic data\twitter
|   category    |string | type of website (News, Shopping etc... )
| location_country_code | string | two digit country code of site origin
|twitter_data| numbers | (followers_count, hashtags_count, likes, links, mentions_count, replies, retweets, total_tweets )
|links_in_count | int | The number of links for this site found on sites
		

#### What I did
- Dealing with multicollinearity using variance inflation factor (VIF) threshold of 5
- Transforming the target variable using log1p
- Creating dummy variable for location + category
- Generate is_weekend attribute from date
- Forward and backward fill for missing values in our dependant variable

