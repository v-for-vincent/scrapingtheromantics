from scrapy.item import Item, Field

class ArticleItem(Item):
    title = Field()
    year = Field()
