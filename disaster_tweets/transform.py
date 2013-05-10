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
import copy
import sys
import traceback
import json
import re

MISSING_VALUE = '!__MISSING_VALUE__!'


def trim_tweet(tweet):
    fields = (
        u'user',
        u'place',
        u'text',
        u'created_at',
        u'coordinates',
        u'id'
    )
    trimmed_tweet = trim_map(tweet, fields)
    trimmed_tweet[u'user'] = trim_user(trimmed_tweet[u'user'])
    return trimmed_tweet


def trim_user(user):
    fields = (
        u'id',
        u'screen_name',
        u'name',
    )
    return trim_map(user, fields)


def trim_map(src, fields, dst=None):
    #fields = map(lambda x: unicode(x, 'utf-8'), fields)
    if not dst:
        dst = {}

    for field in fields:
        if(field in src):
            dst[field] = src[field]
        else:
            dst[field] = MISSING_VALUE
    return dst


class Decorator:

    def __init__(self, name):
        self.name = name

    def decorate(self, trimmed_tweet, original_tweet):
        return trimmed_tweet

    def log_error(self, error_msg):
        sys.stderr.write('ERROR (%s): %s\n' % (self.name, error_msg))


class RemoveHandle(Decorator):

    def __init__(self, name):
        Decorator.__init__(self, name)
        self.handle_re = re.replace('^(d \S+\s+|\S+\s+)')

    def decorate(self, trimmed_tweet, original_tweet):
        text = original_tweet[u'text']
        pretty_text = self.handle_re.sub('', text)
        trimmed_tweet[u'pretty_text'] = pretty_text
        return trimmed_tweet


def decorate_tweet(trimmed_tweet, original_tweet, decorators):
    # add in RemoveHandle before everything else runs so
    # that pretty_text can be used throughout the Decorators
    decorators.insert(0, RemoveHandle('remove handle'))
    for decorator in decorators:
        try:
            scratch_copy = copy.deepcopy(trimmed_tweet)
            scratch_copy = decorator.decorate(scratch_copy, original_tweet)
            if scratch_copy:
                trimmed_tweet = scratch_copy
            else:
                sys.stderr.write('Got back null decorated tweet from %s. Input JSON:\n%s\n' % (decorator.name, json.dumps(trimmed_tweet, indent=4)))
        except Exception, e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # drop this decorator
            sys.stderr.write('decorator "%s" failed (skipping): %s\n' % (decorator.name, e))
            traceback.print_exc(file=sys.stderr)
            sys.stderr.write('Tweet JSON:\n%s' % json.dumps(trimmed_tweet, indent=3))

    return trimmed_tweet
