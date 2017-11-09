#!/usr/bin/env python3
#
#
# date:     Tue 19 Sep 2017 12:49:56 PM CEST
#
# Author:   Ablakim Giray Uestuen
#
# descr:    Get weather information - using JSON
#           I discovered a handy tool while stuyding in the library
#           credits go the the random stranger -->: https://jsonlint.com/
#           basically it formats json files prettily
#
# Usage:    ./wetter.py  city
#

import json, requests, sys



base_url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = '7f55f5c9cccc96d2b3e263f16069a95b' # Get your API key (APPID) here: http://openweathermap.org/appid


if len(sys.argv) < 2:
    print('Usage: %s city\n' % (sys.argv[0]))
    sys.exit(1)
location = ' '.join(sys.argv[1:])


def theTemperature(city):
    query    = base_url + '?q=%s&units=metric&APPID=%s' % (city, api_key)
    response = requests.get(query)
    try:
        response.raise_for_status()
    except Exception as e:
        print('Error of kind: %s ' % (e))

    weatherData = json.loads(response.text)
    print('current weather for %s:\n\n' % location.lower())
    print(weatherData['weather'][0]['main'], '-' ,weatherData['weather'][0]['description'])
    print('temperature ' ,weatherData['main']['temp'], ' celsius')


theTemperature(location)
