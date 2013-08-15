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
import json
import oauth2 as oauth

MENTIONS_URL = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'


class TwitterAPI:

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

    def oauth_req(self, url, http_method="GET", post_body="", http_headers=""):
        consumer = oauth.Consumer(self.consumer_key, self.consumer_secret)
        token = oauth.Token(self.access_token, self.access_secret)
        client = oauth.Client(consumer, token)

        resp, content = client.request(
            url,
            method=http_method,
            body=post_body,
            headers=http_headers
            #force_auth_header=True
        )


        if resp['status'] != '200':
            try:
                error_obj = json.loads(content)
                formatted_error = json.dumps(error_obj, indent=3)
                raise 'Twitter API access error: %s\n%s' % (resp['status'], formatted_error)
            except ValueError:
                raise 'Twitter API access error: %s\n%s' % (resp['status'], content)

        return (resp, content)

    def get_mentions(self, max_id=1):
        max_id_param = ''
        if (max_id > 0):
            max_id_param = 'since_id=%s&' % max_id
        (metadata, mentions_json) = self.oauth_req('%s?%scontributor_details=true' % (MENTIONS_URL, max_id_param))
        print 'hi'
        return mentions_json
