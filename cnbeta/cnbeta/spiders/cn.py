# -*- coding:utf-8 -*-
# -*- coding:gbk2312 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from cnbeta.items import CnbetaItem
import sys
sys.stdout = open('output.txt','w')
class CBSpider(CrawlSpider):
    name = 'cnbeta'
    allowed_domains = ['cnbeta.com']
    start_urls = ['http://www.cnbeta.com']

    rules = (
        Rule(SgmlLinkExtractor(allow=('/articles/.*\.htm', )),
             callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        item = CnbetaItem()
        sel = Selector(response)
        item['title'] = sel.xpath('//title/text()').extract()[0]#.encode('utf-8')
        item['url'] = response.url
        print item['title'].encode('utf-8')
        print item['url']
        return item
