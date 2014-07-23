import twitter
import json

CONSUMER_KEY = 'CxT0uevMd2EsjqM5rNRDM9VlW'
CONSUMER_SECRET = 'u7EcEpvOVjlSjDFkfqN7gl4r1pau59I4txvPQgDOSksf5JEzw4'
OAUTH_TOKEN = '535814971-q66nrKX1BLvCQes6q8wPxwNlKvNV83DehNd5LE4M'
OAUTH_TOKEN_SECRET = 'wXeZV751OjZof5xkRVzvo7MoDLgs4t9jWVQh0ibSWrgtH'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = '#MentionSomeoneImportantForYou'
count = 100

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

status_texts = [ status['text']
for status in statuses]

screen_names = [user_mention['screen_name']
for status in statuses
for user_mention in status['entities']['user_mentions']]

hashtags = [hashtag['text']
for status in statuses
for hashtag in status['entities']['hashtags']]

#Compute a collection of all words from all tweets
words=[w
for t in status_texts
for w in t.split()]

#explore the 1st 5 items for each...
print json.dumps(status_texts[0:5],indent = 1)
print json.dumps(screen_names[0:5], indent = 1)
print json.dumps(hashtags[0:5], indent = 1)
print json.dumps(words[0:5], indent = 1)
