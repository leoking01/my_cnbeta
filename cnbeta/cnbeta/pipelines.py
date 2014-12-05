# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CnbetaPipeline(object):
    def process_item(self, item, spider):
        return item



from scrapy import log
#from scrapy.core.exceptions import DropItem
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors

import datetime

class MySQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'jibenditu',
                #user = 'user',
                user = 'root',
                #passwd = '******',
                passwd = '',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8'
                #use_unicode = true
        )

    def process_item(self, item, spider):
        
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        
        query.addErrback(self.handle_error)
        return item
  
    def _conditional_insert(self, tx, item):
        if item.get('title'):
            tx.execute("insert into cnbeta (title, url ) values (%s, %s )",
                (item['title'],  item['url'])
            )
         #log.msg("Item stored in db: %s" % item, level=log.DEBUG) 
  
  
    def handle_error(self, e):
        log.err(e)
