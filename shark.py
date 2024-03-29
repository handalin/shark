# -*- coding:utf8 -*-
import urllib2, urllib
import sys
import re

class SharkSearcher():
  def __init__(self):
    self.error_msg = "查理没用...查不到...\nbtw,您听歌的品味真独特.\n您确认格式正确?(歌名 歌手名)"
  
  def process_lrc(self, lrc):
    return ''.join( lrc.split('<br />') )
  
  def feed(self, song, artist=None):
    if not artist: artist = ''
    else: artist = '+' + artist
    myurl = 'http://www.xiami.com/search?key=' + song + artist

    # pretent to be IE. ^O^
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'name':'67',
        'location':'Northampton',
        'language':'Python'}
    headers = { 'User-Agent':user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(myurl, data, headers)
    try:
      html = urllib2.urlopen(req).read()
    except BaseException:
      return self.error_msg
    pattern = r'<td class="song_name"><a target="_blank" href="(.+?)" title="'
    try:
      song_url = re.findall(pattern, html)[0]
    except BaseException:
      return self.error_msg
    
    pattern = r'<div class="lrc_main">([\s\S]+?)</div>'
    req = urllib2.Request('http://www.xiami.com'+song_url, data, headers)
    try:
      html = urllib2.urlopen(req).read()
    except BaseException:
      return self.error_msg
    lrc = re.findall(pattern, html)[0]
    
    return self.process_lrc(lrc)
