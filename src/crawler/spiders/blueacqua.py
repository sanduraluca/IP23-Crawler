import scrapy
from itemloaders import ItemLoader
from scrapy import Selector
from ..items import Product
class BlueAcqua(scrapy.Spider):
    name = 'BlueAcqua'
    start_urls = ['https://www.blueacqua.ro/iasi']
    def parse(self, response):
        products =  response.css('#navbar-collapse > div > nav > ul > li:nth-child(2) > ul > li a::attr(href)').getall()
        for products_page in products[:-1]:
            yield response.follow(products_page, callback=self.products_page)


    def products_page(self, response):
        products = response.css('.views-row').getall()
        for i in products:

            yield from self.scrape_item(Selector(text=i))
    def scrape_item(self, response):
        l = ItemLoader(item=Product(), selector=response)
        l.add_value('restaurant_name', 'Blue Acqua')
        l.add_value('delivery_price', '4.99')
        l.add_value('min_delivery', '40')
        l.add_css('name', '.info h2::text')
        l.add_value('source', 'site')
        l.add_css('price', '.price::text'),

        image = ''
        if response.css('a::attr(href)').get() is not None:
            image = r"https://www.blueacqua.ro/" + response.css('a::attr(href)').get()
        l.add_value('category', '')
        l.add_value('description', '')
        yield l.load_item()
