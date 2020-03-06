# -*- coding: utf-8 -*-
import scrapy


class ItemSpider(scrapy.Spider):

    name = 'ItemSpider'
    allowed_domains = ['yad2.co.il']
    start_urls = ['https://www.yad2.co.il/vehicles/private-cars?page=1']

    def parse(self, response):

        url = response.url
        # Extract total amount of pages
        total_pages = int(response.xpath('//button[@class="page-num"]/text()').get().strip())

        for page in range(2, total_pages):
            page_url = url[:-1] + str(page)
            yield scrapy.Request(page_url, self.parse_listing)

        yield from self.parse_listing(response)

    def parse_listing(self, response):

        for item_id in response.xpath('//div/@item-id').getall():
            yield {
                'item_id': item_id,
                'visited': 0
            }
