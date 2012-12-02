import sys
from disaster_tweets.twitter_api import TwitterAPI
import json
from disaster_tweets.transform import trim_tweet
from disaster_tweets.transform import RemoveHandle
from disaster_tweets.transform import decorate_tweet


(consumer_key, consumer_secret, access_token, access_secret, handle) = sys.argv[1:]
twitter = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)

tweets = twitter.get_mentions()
tweet_objs = json.loads(tweets)
#print tweet_objs[0]
#for key in tweet_objs[0]:
#    print type(key)
#print json.dumps(tweet_objs[0],indent=3)

#decorators = (RemoveHandle('remove handle', handle), ReverseGeoCode('reverse geocode'))
decorators = (RemoveHandle('remove handle', handle),)

trimmed_tweets = map(lambda x: trim_tweet(x), tweet_objs)
decorated_tweets = map(lambda x: decorate_tweet(x, decorators), trimmed_tweets)
print json.dumps(decorated_tweets, indent=3)
