import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes2'

    allowed_domains = ['quotes.toscrape.com']

    start_urls = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2'
            ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open( filename, 'wb' ) as f:
            f.write( response.body )
