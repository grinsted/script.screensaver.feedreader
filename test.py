#!/usr/bin/python


import re
import feedparser
import urllib
import requests
import urlparse
import traceback
import time
import datetime


print time.time()
print datetime.datetime.now().time()

url='sea level rise'


desc = re.sub('(\\w+,?) *\\n(\\w+)','\\1 \\2','ASDF SDF ASDF,\nasddas. ')  
print desc


if url.find('//')<0: #bing mode
    url = "https://www.bing.com/news/search?q=%s&format=RSS" % urllib.quote_plus(url)
    url = requests.get(url, headers={'Accept-Language': 'en-US,en'});
    url = url.content.replace('<News:Image>','<media:thumbnail>')
    url = url.replace('</News:Image>','&amp;sz=1920x720</media:thumbnail>')
    #url = 'https://news.google.com/news/feeds?pz=1&cf=all&q=%s&hl=en&output=rss' % urllib.quote_plus(url)

    #url = 'https://news.google.com/news/feeds?pz=1&cf=all&q=%s&hl=en&output=rss' % urllib.quote_plus(url)
feed = feedparser.parse(url)

item = feed.entries[0]
