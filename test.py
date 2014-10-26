#!/usr/bin/python


import re
import feedparser
import urllib
import requests
import urlparse


url='sea level rise'

if url.find('//')<0: #bing mode
    url = "https://www.bing.com/news/search?q=%s&format=RSS" % urllib.quote_plus(url)
    url = requests.get(url, headers={'Accept-Language': 'en-US,en'});
    url = url.content.replace('<News:Image>','<media:thumbnail>')
    url = url.replace('</News:Image>','&amp;sz=1920x720</media:thumbnail>')
    #url = 'https://news.google.com/news/feeds?pz=1&cf=all&q=%s&hl=en&output=rss' % urllib.quote_plus(url)

    #url = 'https://news.google.com/news/feeds?pz=1&cf=all&q=%s&hl=en&output=rss' % urllib.quote_plus(url)
feed = feedparser.parse(url)

for item in feed.entries:
    if 'media_thumbnail' in item:
        cimg =item.media_thumbnail[0]['url']
        
        imgparsed = urlparse.urlparse(cimg)
        if imgparsed.path == '/imagenewsfetcher.aspx':
            imgparsed = urlparse.parse_qs(imgparsed.query)
            if 'q' in imgparsed: cimg = imgparsed['q']
            print cimg