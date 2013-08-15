# Disaster Tweet Reports

## Overview #

Disaster Tweet Reports is intended to be a library and webapp that can be used to quickly generate high-quality, geo-coded information when a disaster strikes.  As Ushahidi proved in the wake of the Haiti earthquake in 2009, SMS can be used to gather small snippets of information.  However, it lacks a lot of the context needed to efficiently use that information to drive disaster response.  Modern mobile Twitter clients, like Twitter's iOS and Android apps or third-party apps like Tweetdeck and Tweetbot are familiar, user-friendly applications that can generate geocoded data very simply and most likely are already installed on a user's phone.

The basic archictecture here is:

1.  Create a new twitter handle to collect reports
1.  instruct disaster response personnel/volunteers to direct message reports to the twitter handle
1.  deploy disaster_tweet_reports to filter, and post-process the tweet stream into usable information
1.  ingest that information into some other system to handle the dispatching of work crews, first-responders, etc.

## The Need For High Quality Disaster Reports

Effective disaster recovery is aided by quick and accurate damage assements so that volunteers and material can be efficiently
put to use in a timely manner.  Smartphones make a great tool for crafting reports that contain geocoordinates obtained from GPS
hardware, including photos that are stamped with geocoordinates (lat/long).  However, building special purpose software for this task to work 
across handsets of all different types is a pretty herculean task - much more ideal to come up a with a reporting protocol that will
work with pretty much any combination of hardware and operating system.

Enter Twitter as a platform for disaster reporting - Twitter clients are already maintained for almost every handset in existence and most
of them allow the direct attachment of geocoordinates to a tweet.  Twitter clients also handle the upload and attachment of photos to tweets.
Given this, Twitter makes a great conduit for getting high quality reports as part of disaster recovery operations.

## Constraints On Such A System

* Disaster reports can contain sensitive, personally identifiable information (PII) about people at their most vulnerable.  Rather than wanting
to provide looters and predatory contractors with public information about where to focus their malicious efforts, we use direct messages to keep
the data private.
* 140 characters (less when inluding image urls for uploaded photos) can be a pretty tight bound on a disaster report.  However, it turns out that
most disaster recovery reports are very similar as disasters tend to produce clear modalities of damage (like flooding, structural damage, etc). This allows us to create short code dictionaries that allow for a compact notation for most of the data contained in a report.  The software will
then expand the short codes into a more readable format as they come into the system.
* This system will require working wireless data infrastructure.  While this is often the case, very serious damage could make this effort useless
until the data networks are repaired in disaster areas.

## Operational Outline ##

1. Each disaster recovery operation will require the creation of a new (or reuse of an existing) dedicated twitter handle to serve as the endpoint to send direct message traffic to.
2. Once the handle has been created the proper API keys created, the software can be configured and brought up.
3. Volunteers then direct their Twitter account to follow the endpoint handle.  Auto-follow will follow them back (to enable direct messaging) and send them a link to web version of instruction for filing reports on this instance.
4. Tweets begin to flow - recovery happens through the hard work of volunteers

## What The Code Does

While tweets started with humble beginnings as simple SMS messages, the modern tweet is a thing to behold, clocking in at 135 *lines* of pretty-printed JSON data, including everything from the author's icon to geeocordinates to parent tweets in a threaded tweet conversation.

The stated goal of this project is to two things to the data in a disaster report tweet:

1. Trim out all information that's unecessary for disaster recovery operations
2. Decorate the remaining JSON with useful data from other web services
3. Transform the data into simpler data structures or cleaned up text

The ultimate goal being the creation of clean and useful data for ingestion into various disaster management systems.

# Technical Info

## Depends #
* oauth2 - https://github.com/brosner/python-oauth2.git
* httplib2 - http://code.google.com/p/httplib2/
* A twitter handle with an application created on http://dev.twitter.com (see detailed OAuth instructions at https://dev.twitter.com/docs/auth/oauth/single-user-with-examples)

## Future Plans #

* Google Reverse Geocoder integration if legal means can be found (code written, waiting on legal ideas)
* Short code expand to allow for high-density twitter messages
* Downloading and including image data in final JSON blob for easy integration of imagery
* Better documentation around setting up and deploying in an operational situation

### Short Term Work To Done

Getting to an minimal viable product will need the following things:

1. A working Django app to display, download, and make available via API all the collected tweets
2. The devops and packaging work to make this as simple and robust as possible to deploy
3. The data pipe that will periodically and reliably pull the data from twitter
4. Various administrative modules to do things like auto-follow accounts and send out instructions
5. Operations time documentation on setting up and operating the system in a real disaster scenario

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



