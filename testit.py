#!/usr/bin/python

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

from disaster_tweets.twitter_api import TwitterAPI
import json
from disaster_tweets.transform import trim_tweet
from disaster_tweets.transform import decorate_tweet
from disaster_tweets.GoogleReverseGeocoder import GoogleReverseGeocoder
from disaster_tweets.TwimgImageDataDecorator import TwimgImageDataDecorate

# read the keys from a file (that's not in git)
execfile('keys.txt')

handle = 'MITHackersWB'

# parameters loaded from keys.txt
twitter = TwitterAPI(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_secret)
tweets = twitter.get_mentions()
tweet_objs = json.loads(tweets)
#print tweet_objs[0]
#for key in tweet_objs[0]:
#    print type(key)
#print json.dumps(tweet_objs[0], indent=3)

#decorators = (RemoveHandle('remove handle', handle), ReverseGeoCode('reverse geocode'))
decorators = (GoogleReverseGeocoder(), TwimgImageDataDecorate())

for tweet in tweet_objs:

    # output then process then output to make errors easier to isolate

    print '==========================================================='
    print 'Original Tweet:'
    print ''
    print json.dumps(tweet, indent=4)
    print ''
    print '=== end Original Tweet ===================================='
    print '==========================================================='

    trimmed_tweet = trim_tweet(tweet)

    print '***********************************************************'
    print 'Trimmed Tweet:'
    print ''
    print json.dumps(trimmed_tweet, indent=4)
    print ''
    print '*** end Trimmed Tweet *************************************'
    print '***********************************************************'

    decorated_tweet = decorate_tweet(trimmed_tweet, tweet, decorators)

    print '-----------------------------------------------------------'
    print 'Decorated Tweet:'
    print ''
    print json.dumps(decorated_tweet, indent=4)
    print ''
    print '--- end Decorated Tweet -------------------------------------'
    print '-----------------------------------------------------------'
