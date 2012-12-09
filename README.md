## Depends #
* oauth2 - https://github.com/brosner/python-oauth2.git
* httplib2 - http://code.google.com/p/httplib2/
* A twitter handle with an application created on http://dev.twitter.com (see detailed OAuth instructions at https://dev.twitter.com/docs/auth/oauth/single-user-with-examples)

## Future Plans #

* Google Reverse Geocoder integration if legal means can be found (code written, waiting on legal ideas)
* Short code expand to allow for high-density twitter messages
* Downloading and including image data in final JSON blob for easy integration of imagery
* Better documentation around setting up and deploying in an operational situation

## Example output

Here's an example using the default trimming routines along with the Google Reverse Geocoder:


	===========================================================
	Original Tweet:
	
	{
	    "user": {
	        "follow_request_sent": false, 
	        "profile_use_background_image": false, 
	        "default_profile_image": false, 
	        "id": 14574697, 
	        "verified": false, 
	        "profile_text_color": "87BC44", 
	        "profile_image_url_https": "https://si0.twimg.com/profile_images/263656347/regs-benjy-monkey-portrait_normal.jpg", 
	        "profile_sidebar_fill_color": "E0FF92", 
	        "entities": {
	            "url": {
	                "urls": [
	                    {
	                        "url": "http://node.realityspline.net/ari/", 
	                        "indices": [
	                            0, 
	                            34
	                        ], 
	                        "expanded_url": null
	                    }
	                ]
	            }, 
	            "description": {
	                "urls": []
	            }
	        }, 
	        "followers_count": 694, 
	        "profile_sidebar_border_color": "87BC44", 
	        "id_str": "14574697", 
	        "profile_background_color": "000000", 
	        "listed_count": 29, 
	        "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png", 
	        "utc_offset": -28800, 
	        "statuses_count": 2588, 
	        "description": "Senior Software Engineer and blogger at Palantir Technologies (@PalantirTech)  I used to be named Ari Gordon-Schlosberg; an explanation: http://bit.ly/c40tHM", 
	        "friends_count": 613, 
	        "location": "SF, Palo Alto, or elsewhere", 
	        "profile_link_color": "5555FF", 
	        "profile_image_url": "http://a0.twimg.com/profile_images/263656347/regs-benjy-monkey-portrait_normal.jpg", 
	        "following": null, 
	        "geo_enabled": true, 
	        "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png", 
	        "screen_name": "alephbass", 
	        "lang": "en", 
	        "profile_background_tile": false, 
	        "favourites_count": 107, 
	        "name": "Ari Gesher", 
	        "notifications": null, 
	        "url": "http://node.realityspline.net/ari/", 
	        "created_at": "Mon Apr 28 20:05:10 +0000 2008", 
	        "contributors_enabled": false, 
	        "time_zone": "Pacific Time (US & Canada)", 
	        "protected": false, 
	        "default_profile": false, 
	        "is_translator": false
	    }, 
	    "favorited": false, 
	    "entities": {
	        "user_mentions": [
	            {
	                "id": 428902058, 
	                "indices": [
	                    0, 
	                    10
	                ], 
	                "id_str": "428902058", 
	                "screen_name": "GesherAPI", 
	                "name": "Gesher API"
	            }
	        ], 
	        "hashtags": [], 
	        "urls": []
	    }, 
	    "contributors": null, 
	    "truncated": false, 
	    "text": "@gesherapi now a tweet with coords instead of places", 
	    "created_at": "Sun Dec 02 17:42:06 +0000 2012", 
	    "retweeted": false, 
	    "in_reply_to_status_id_str": null, 
	    "coordinates": {
	        "type": "Point", 
	        "coordinates": [
	            -73.98982193, 
	            40.73938768
	        ]
	    }, 
	    "in_reply_to_user_id_str": "428902058", 
	    "source": "<a href=\"http://tapbots.com/tweetbot\" rel=\"nofollow\">Tweetbot for iOS</a>", 
	    "in_reply_to_status_id": null, 
	    "in_reply_to_screen_name": "GesherAPI", 
	    "id_str": "275293780956045312", 
	    "place": {
	        "full_name": "Manhattan, NY", 
	        "url": "https://api.twitter.com/1.1/geo/id/086752cb03de1d5d.json", 
	        "country": "United States", 
	        "place_type": "city", 
	        "bounding_box": {
	            "type": "Polygon", 
	            "coordinates": [
	                [
	                    [
	                        -74.047285, 
	                        40.679548
	                    ], 
	                    [
	                        -73.907, 
	                        40.679548
	                    ], 
	                    [
	                        -73.907, 
	                        40.882214
	                    ], 
	                    [
	                        -74.047285, 
	                        40.882214
	                    ]
	                ]
	            ]
	        }, 
	        "country_code": "US", 
	        "attributes": {}, 
	        "id": "086752cb03de1d5d", 
	        "name": "Manhattan"
	    }, 
	    "retweet_count": 0, 
	    "geo": {
	        "type": "Point", 
	        "coordinates": [
	            40.73938768, 
	            -73.98982193
	        ]
	    }, 
	    "id": 275293780956045312, 
	    "in_reply_to_user_id": 428902058
	}
	
	=== end Original Tweet ====================================
	===========================================================
	***********************************************************
	Trimmed Tweet:
	
	{
	    "text": "@gesherapi now a tweet with coords instead of places", 
	    "created_at": "Sun Dec 02 17:42:06 +0000 2012", 
	    "place": {
	        "full_name": "Manhattan, NY", 
	        "url": "https://api.twitter.com/1.1/geo/id/086752cb03de1d5d.json", 
	        "country": "United States", 
	        "place_type": "city", 
	        "bounding_box": {
	            "type": "Polygon", 
	            "coordinates": [
	                [
	                    [
	                        -74.047285, 
	                        40.679548
	                    ], 
	                    [
	                        -73.907, 
	                        40.679548
	                    ], 
	                    [
	                        -73.907, 
	                        40.882214
	                    ], 
	                    [
	                        -74.047285, 
	                        40.882214
	                    ]
	                ]
	            ]
	        }, 
	        "country_code": "US", 
	        "attributes": {}, 
	        "id": "086752cb03de1d5d", 
	        "name": "Manhattan"
	    }, 
	    "user": {
	        "id": 14574697, 
	        "name": "Ari Gesher", 
	        "screen_name": "alephbass"
	    }, 
	    "coordinates": {
	        "type": "Point", 
	        "coordinates": [
	            -73.98982193, 
	            40.73938768
	        ]
	    }
	}
	
	*** end Trimmed Tweet *************************************
	***********************************************************
	-----------------------------------------------------------
	Decorated Tweet:
	
	{
	    "address_best_guess_pretty": "907 Broadway, New York, NY 10003, USA", 
	    "text": "@gesherapi now a tweet with coords instead of places", 
	    "created_at": "Sun Dec 02 17:42:06 +0000 2012", 
	    "coordinates": {
	        "type": "Point", 
	        "coordinates": [
	            40.73938768, 
	            -73.98982193
	        ]
	    }, 
	    "place": {
	        "full_name": "Manhattan, NY", 
	        "url": "https://api.twitter.com/1.1/geo/id/086752cb03de1d5d.json", 
	        "country": "United States", 
	        "place_type": "city", 
	        "bounding_box": {
	            "type": "Polygon", 
	            "coordinates": [
	                [
	                    [
	                        -74.047285, 
	                        40.679548
	                    ], 
	                    [
	                        -73.907, 
	                        40.679548
	                    ], 
	                    [
	                        -73.907, 
	                        40.882214
	                    ], 
	                    [
	                        -74.047285, 
	                        40.882214
	                    ]
	                ]
	            ]
	        }, 
	        "country_code": "US", 
	        "attributes": {}, 
	        "id": "086752cb03de1d5d", 
	        "name": "Manhattan"
	    }, 
	    "user": {
	        "screen_name": "alephbass", 
	        "name": "Ari Gesher", 
	        "id": 14574697
	    }, 
	    "addresses_formatted": [
	        "907 Broadway, New York, NY 10003, USA", 
	        "Flatiron District, New York, NY, USA", 
	        "New York, NY 10010, USA", 
	        "Midtown, New York, NY, USA", 
	        "New York, NY, USA", 
	        "Manhattan, New York, NY, USA", 
	        "New York, NY, USA", 
	        "New York, USA", 
	        "United States"
	    ], 
	    "pretty_text": "now a tweet with coords instead of places", 
	    "address_best_guess_structured": [
	        {
	            "street_number": "907"
	        }, 
	        {
	            "route": "Broadway"
	        }, 
	        {
	            "neighborhood": "Flatiron District"
	        }, 
	        {
	            "sublocality": "Manhattan"
	        }, 
	        {
	            "locality": "New York"
	        }, 
	        {
	            "administrative_area_level_2": "New York"
	        }, 
	        {
	            "administrative_area_level_1": "NY"
	        }, 
	        {
	            "country": "US"
	        }, 
	        {
	            "postal_code": "10003"
	        }
	    ]
	}
	
	--- end Decorated Tweet -------------------------------------
	-----------------------------------------------------------

## License #

Disaster Tweet Reports is made available under the Apache 2.0 License.

>Copyright 2012 Palantir Technologies
>
>Licensed under the Apache License, Version 2.0 (the "License");
>you may not use this file except in compliance with the License.
>You may obtain a copy of the License at
>
><http://www.apache.org/licenses/LICENSE-2.0>
>
>Unless required by applicable law or agreed to in writing, software
>distributed under the License is distributed on an "AS IS" BASIS,
>WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
>See the License for the specific language governing permissions and
>limitations under the License.



