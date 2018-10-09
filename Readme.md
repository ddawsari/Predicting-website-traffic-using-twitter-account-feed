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

