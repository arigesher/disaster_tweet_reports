# TODO - features to be added #

## Operationalize Tweet Processing

1. Current library is just run in test mode to pull tweets - it needs to be built into a proper daemon that pulls, decorates, and stores tweets
1. CSV and JSON export 
1. Implement auto-follow using Twitter APIs
1.1. auto-follow should send link to online version of short code cheat sheets

## Standalone Web Operation ##

1. Build web application that can do display of the decorated tweets, including displaying the geocoded data in compliance with the Google APIs
1. Output of all collected data into Google Maps
1. Work on deployment issues so that an instance can be brought up for a disaster in a pushbutton manner


## End User Documentation ##
1. Well-formatted documentation for end users detailing how to set up the system
1.1. Setting up a twitter handle for the disaster endpoint
1.1. Helping volunteers setup a twitter handle and following the disaster endpoint
1.1. Setting up auto-follow
1.1. Configuring popular Twitter clients on iOS, Android, and RIM to do proper geostamped tweets
1.1. Look into twitter clients that store geocoords in tweet drafts for offline use
1. Work with Team Rubicon to build up a set of pre-defined short code dictionaries related to known disaster types
1. Write code to produce printable short code dictionary cheatsheets