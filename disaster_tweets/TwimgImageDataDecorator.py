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

import httplib2
import base64
from transform import Decorator


class TwimgImageDataDecorate(Decorator):

    def __init__(self, sizes=['large'], thumbnail=True):
        Decorator.__init__(self, 'Twitter Image Data Decorator')
        self.sizes = sizes
        self.thumbnail = thumbnail

    def decorate(self, trimmed_tweet, original_tweet):
        if u'entities' in original_tweet and u'media' in original_tweet[u'entities']:
            media = original_tweet[u'entities'][u'media'][0]
            media_url = media[u'media_url']
            images = {}
            for size in self.sizes:
                url = '%s:%s' % (media_url, size)
                image_data = self.grab_image_data(url)
                if image_data:
                    images[size] = image_data
            if images:
                trimmed_tweet[u'images'] = images

            thumbnail = self.grab_image_data('%s:%s' % (url, 'thumb'))
            if thumbnail:
                trimmed_tweet[u'thumbnail'] = thumbnail
        else:
            print self.log_error("no image data in %s" % trimmed_tweet[u'id'])
        return trimmed_tweet

    def grab_image_data(self, url):
        try:
            h = httplib2.Http()
            resp, content = h.request(url)
            if resp['status'] == '200':
                return base64.b64encode(content)
        except Exception, e:
            self.log_error("Error loading image from %s: %s" % (url, e))
        return None
