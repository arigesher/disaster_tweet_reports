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
import httplib2
from transform import Decorator

API_URL = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%s&sensor=false"

'''
NOTE: IT'S NOT CLEAR UNDER WHAT LEGAL TERMS THIS CAN BE USED

Use of this code without written permission from Google violates
the terms of service of the Google Map APIs.

See:

Specifically: 10.1.1 (g) from https://developers.google.com/maps/terms#section_10_12

    No Use of Content without a Google Map. You must not use
    or display the Content without a corresponding Google map,
    unless you are explicitly permitted to do so in the Maps
    APIs Documentation, or through written permission from
    Google. In any event, you must not use or display the
    Content on or in conjunction with a non-Google map. For
    example, you must not use geocodes obtained through the
    Service in conjunction with a non-Google map. As another
    example, you must not display Street View imagery alongside
    a non-Google map, but you may display Street View imagery
    without a corresponding Google map because the Maps APIs
    Documentation explicitly permits you to do so.

Please make sure to use this code legally and obtain written
permission from Google to use their APIs for your disaster
relief application.

Otherwise, make sure to leave this decorator out of your
decorator stack.

'''


class GoogleReverseGeocoder(Decorator):

    def __init__(self, attach_full_info=False):
        Decorator.__init__(self, "Google Reverse Geocoder")
        self.attach_full_info = attach_full_info

    def decorate(self, trimmed_tweet, original_tweet):
        ''' Coordinates JSON block in tweet looks like this:

            "coordinates": {
                "type": "Point",
                "coordinates": [
                    -73.98982193,
                    40.73938768
                ]
            }
        '''
        # make sure we have what we need
        if u'coordinates' in trimmed_tweet:
            coordinate_obj = trimmed_tweet[u'coordinates']
            if coordinate_obj and u'type' in coordinate_obj and coordinate_obj[u'type'] == u'Point':
                if u'coordinates' in coordinate_obj:
                    longlat = coordinate_obj[u'coordinates']
                    coordinates = longlat.reverse()
                    coordinates = ",".join(map(lambda x: str(x), longlat))
                    self.reverse_geocode_tweet(trimmed_tweet, coordinates)
                    return trimmed_tweet
        # when in doubt, just return the unchanged trimmed_tweet
        return trimmed_tweet

    def reverse_geocode_tweet(self, tweet, coordinates):
        http = httplib2.Http()
        url = API_URL % coordinates
        resp, content = http.request(url, "GET")

        if resp['status'] != '200':
            try:
                error_obj = json.loads(content)
                formatted_error = json.dumps(error_obj, indent=3)
                raise 'Google API access error: %s\n%s' % (resp['status'], formatted_error)
            except ValueError:
                raise 'Google API access error: %s\n%s' % (resp['status'], content)
        else:
            geocoder_output = json.loads(content)

            best_guess = geocoder_output[u'results'][0]
            tweet[u'address_best_guess_pretty'] = best_guess[u'formatted_address']
            tweet[u'address_best_guess_structured'] = self.transform_address(best_guess[u'address_components'])

            addresses = []
            for result in geocoder_output[u'results']:
                addresses.append(result[u'formatted_address'])
            if len(addresses) > 0:
                tweet[u'addresses_formatted'] = addresses
            if self.attach_full_info:
                tweet[u'google_reverse_geocoder_output'] = geocoder_output[u'results']

    def transform_address(self, address_block):
        '''

        JSON block for Google address structure we're transforming:

        "address_components" : [
            {
               "long_name" : "285",
               "short_name" : "285",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Bedford Ave",
               "short_name" : "Bedford Ave",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Williamsburg",
               "short_name" : "Williamsburg",
               "types" : [ "neighborhood", "political" ]
            },
            {
               "long_name" : "Brooklyn",
               "short_name" : "Brooklyn",
               "types" : [ "sublocality", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "New York",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Kings",
               "short_name" : "Kings",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "NY",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "11211",
               "short_name" : "11211",
               "types" : [ "postal_code" ]
            }
         ],
        '''

        simple_structured_address = []
        for component in address_block:
            value = component[u'short_name']
            label = component[u'types'][0]

            simple_structured_address.append({label: value})
        return simple_structured_address
