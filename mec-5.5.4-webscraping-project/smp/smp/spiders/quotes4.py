import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes4"
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            ]

    def parse(self, response):
        for quote in response.xpath('//*[contains(@class, "quote")]'):
            yield {
                    'text': quote.xpath('.//span[contains(@class, "text")]/text()').get(),
                    'author': quote.xpath('.//small/text()').get(),
                    'tags': quote.xpath('.//*[@class="tag"]/text()').getall(),
                    }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
