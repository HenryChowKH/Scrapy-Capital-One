# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

from scrapy.item import Item, Field


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #Product Name
    Name = scrapy.Field()
    #Image Path URL
    Path = scrapy.Field()
    #Website Url
    Source = scrapy.Field()
    #Price
    Cost = scrapy.Field()
    		
	
