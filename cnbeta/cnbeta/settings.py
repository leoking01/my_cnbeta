# -*- coding: utf-8 -*-

# Scrapy settings for cnbeta project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cnbeta'

SPIDER_MODULES = ['cnbeta.spiders']
NEWSPIDER_MODULE = 'cnbeta.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cnbeta (+http://www.yourdomain.com)'
ITEM_PIPELINES=['cnbeta.pipelines.MySQLStorePipeline']
