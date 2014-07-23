import twitter
import json


CONSUMER_KEY = ' '
CONSUMER_SECRET = ' '
OAUTH_TOKEN = ' '
OAUTH_TOKEN_SECRET = ' '

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = '#MentionSomeoneImportantForYou'
count = 100

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

#Iterate through 5 more batches of results by following the cursor

for _ in range(5):
	print "Length of statuses", len(statuses)
	try:
		next_results = search_results['search_metadata']['next_results']
	except KeyError, e: #No more results when next_results doesn't exist
		break
		# Create a dictionary from next_results, which has the following form:
		# ?max_id=313519052523986943&q=NCAA&include_entities=1
		kwargs = dict([kv.split('=') for kv in next_results[1:].split("&") ])
			
		search_results = twitter_api.search.tweets(**kwargs)
		statuses += search_results['statuses']
	# Show one sample search result by slicing the list...
	print json.dumps(statuses[0], indent=1)
