#!/usr/bin/python
# -*- coding: UTF-8 -*-
# #html下载器

import urllib2

class HtmlDownloder(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
