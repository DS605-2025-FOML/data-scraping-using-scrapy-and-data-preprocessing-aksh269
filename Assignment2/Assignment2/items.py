# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Assignment2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    rating_of_book=scrapy.Field()
    availbility_of_book=scrapy.Field()
    price_of_book=scrapy.Field()
    bookimage_url=scrapy.Field()
