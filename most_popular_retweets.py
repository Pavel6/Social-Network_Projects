import twitter
from prettytable import PrettyTable

CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
OAUTH_TOKEN = 'XXXX'
OAUTH_TOKEN_SECRET = 'XXXX'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = '#MentionSomeoneImportantForYou'   #can replace this with anything
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

retweets = [
# Store out a tuple of these three values ...
(status['retweet_count'],
status['retweeted_status']['user']['screen_name'],
status['text'])

# ... for each status ...
for status in statuses

# ... so long as the status meets this condition.
	if status.has_key('retweeted_status')
]	
#Slice off the first 5 from the sorted results and display each item in the tuple.

pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[ pt.add_row(row) for row in sorted(retweets, reverse=True)[:5] ]
pt.max_width['Text'] = 50
pt.align= 'l'
print pt
