#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
目标：百度百科python词条相关词条网页--标题和简介
入口页：https://baike.baidu.com/item/Python/407313?fr=aladdin#1
url格式：--词条页面url：/view/125370.htm
数据格式：
 --标题：<dd class="lemmaWgt-lemmaTitle-title"></dd>
 --简介：<div class="para" label-module="para">Python的创始人为Guido van Rossum。</div>
页面编码：UTF8

"""
#调度程序

import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloder()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1  # 记录当前爬取的是第几个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 取一个出来
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)  # 下载对应的页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 页面解析
                self.urls.add_new_urls(new_urls)  # 添加了变量的new_url上面是set new——url
                self.outputer.collect_data(new_data)  # 收集数据

                if count >= 1000:
                    break
                count += 1
            except Exception as e:
                print(str(e))
                print 'craw failed'
            #写入文件
            self.outputer.output_html()
            #写入数据库
            #self.outputer.output_mysql()


if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

