#!/usr/bin/python
# -*- coding: UTF-8 -*-
# #html下载器

import urllib2

class HtmlDownloder(object):
    def download(self, url):
        if url is None:
            return None

        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        headers = { 'User-Agent' : user_agent }
        
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)

        if response.getcode() != 200:
            return None

        return response.read()
