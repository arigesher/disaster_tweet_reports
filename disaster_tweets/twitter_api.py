import json
import oauth2 as oauth

MENTIONS_URL = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'


class TwitterAPI:

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

    def oauth_req(self, url, http_method="GET", post_body=None, http_headers=None):
        consumer = oauth.Consumer(self.consumer_key, self.consumer_secret)
        token = oauth.Token(self.access_token, self.access_secret)
        client = oauth.Client(consumer, token)

        resp, content = client.request(
            url,
            method=http_method,
            body=post_body,
            headers=http_headers,
            force_auth_header=True
        )

        return content

    def get_mentions(self, max_id):
        mentions_json = self.oauth_req('%s?since_id=%scontributor_details=true' % (MENTIONS_URL, max_id))
        
        mentions = json.loads(mentions_json)

