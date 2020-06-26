# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class weatherItem(scrapy.Item):
    city = scrapy.Field()
    temper = scrapy.Field()
    date = scrapy.Field()
    #humidity = scrapy.Field()
    windSpeed = scrapy.Field()
    weather = scrapy.Field()
    #rainProb = scrapy.Field()
