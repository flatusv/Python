#!/usr/bin/env python3
#
# author:   Ablakim Giray Üstün
# date:     Tue 15 May 2018 02:01:13 PM CEST
#
# descr:    Retrieve and download the most recent tracks from "weareone.fm"




import os
import youtube_dl
import requests
import re
import urllib.request
import urllib.parse
import sys
from bs4 import BeautifulSoup
from pathlib import Path

# Global variables
logFilePath = 'path/where/of/log_file'
logFile = logFilePath + sys.argv[1] + "_history.log"
radio = ["technobase", "housetime", "hardbase", "trancebase", "coretime",
         "clubtime","teatime"]



# def createHistoryLog():
#         os.system("touch {}".format(logFile))
#         print("Created log file: {}".format(logFile))




class Tracklist():

    def __init__(self, url):
        self.url = url
        self.tempList = []
        self.tracks = []


    def getListOfTracks(self, fname):
        '''
        get all the unique tracks..
        '''

        # processing and parsing
        r = requests.get(self.url)
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html5lib')
        links = soup.findAll('a', href=re.compile('^/release/'))
        self.tempList = list(set(list(filter(None,[ x.text for x in links ]))))

        # not get rid of duplicates
        with open(fname) as f:
            content = f.readlines()
        alreadyDownloaded = [track.replace('\n','') for track in content]
        self.tracks = [ track for track in self.tempList if track not in alreadyDownloaded ]
        return self.tracks


    def ytDownTracks(self):
        '''
        ..and keep track of the downloaded songs,by puting their names in a radio specific history file
        '''
        for track in self.tracks: # gvsearch uses google video, change it to "ytsearch" to use youtube
            with open(logFile, 'a') as f:
                os.system('youtube-dl --extract-audio --audio-format mp3 -o "{}.%(ext)s" "ytsearch1:{}"'.format(track,track))
                f.write(track + "\n")   # write the track title to log file


if __name__== "__main__":

    if (len(sys.argv) != 1 and sys.argv[1] not in radio):
        print("Usage: {} {}".format(sys.argv[0],radio))
        sys.exit(0)
    else:
        tracklist = Tracklist("https://www.{}.fm/tracklist/".format(sys.argv[1]))
        tracklist.getListOfTracks(logFile)
        tracklist.ytDownTracks()
