import twitter
import json
import pprint
import re

CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
OAUTH_TOKEN = 'XXXX'
OAUTH_TOKEN_SECRET = 'XXXX
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = '#MentionSomeoneImportantForYou'
count = 10

_retweets = twitter_api.statuses.retweets(id=XXXX)
print [r['user']['screen_name'] for r in _retweets]
