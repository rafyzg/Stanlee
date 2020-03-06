# -*- coding: utf-8 -*-
import scrapy


class Item(scrapy.Item):
    item_id = scrapy.Field()
    visited = scrapy.Field()    # 0 - No , 1 - Yes


# Represents all car types - mini, sedan, SUV etc..
class Car(scrapy.Item):
    manufacturer = scrapy.Field()
    model = scrapy.Field()
    type = scrapy.Field()
    color = scrapy.Field()
    year = scrapy.Field()
    hand = scrapy.Field()
    doors = scrapy.Field()
    mileage = scrapy.Field()
    engine = scrapy.Field()
    engine_size = scrapy.Field()
    transmission = scrapy.Field()


class Motorcycle(scrapy.Item):
    manufacturer = scrapy.Field()
    model = scrapy.Field()
    color = scrapy.Field()
    hand = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    engine_size = scrapy.Field()

