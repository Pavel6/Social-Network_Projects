#Connects to twitter and finds latest trends or popular posts on twitter and then returns them in a readable format.

import twitter
import json


CONSUMER_KEY = ' '
CONSUMER_SECRET = ' '
OAUTH_TOKEN = ' '
OAUTH_TOKEN_SECRET = ' '   #Make an an app at https://apps.twitter.com/  and from the apps page you can request 
                           #these values I left blank

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#Nothing to see by displaying twitter_api except that it's now a 
#defined variable.

#print twitter_api

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id = WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

#print world_trends   
#print 
#print us_trends   (This returns what we want but in very difficult to read format.

#print json.dumps(world_trends,indent=1)
#print
#print json.dumps(us_trends, indent=1)   (Returns what we want but there are some duplicates)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])
common_trends = world_trends_set.intersection(us_trends_set)
print common_trends
#Returns best format I found so far.
