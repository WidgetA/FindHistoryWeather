# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindweatherScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 'date': date,
    # 'statu': statu,
    # 'temperature': temperature,
    # 'wind': wind
    date = scrapy.Field()
    statu = scrapy.Field()
    temperature = scrapy.Field()
    wind = scrapy.Field()
    pass
