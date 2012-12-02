#   Copyright 2012 Palantir Technologies
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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
