# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class Prof(Item):
    content=Field()    
    def __str__(self):
        return "item [content=%s; ]" % (self["content"])

