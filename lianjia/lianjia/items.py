# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()  # 价格
    per_price = scrapy.Field()  # 每平米价格
    style = scrapy.Field()  # 房子户型
    house_size = scrapy.Field()  # 房屋平米数
    region = scrapy.Field()  # 房子地点
    focus = scrapy.Field()  # 关注人数
    establish_year = scrapy.Field()  # 建立房子的年限
    floor = scrapy.Field()  #层数