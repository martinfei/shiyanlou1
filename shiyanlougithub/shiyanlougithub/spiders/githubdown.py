# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import GithubItem

class GithubdownSpider(scrapy.Spider):
    name = 'githubdown'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for gt in response.css('li.col-12'):
            item = GithubItem(
                    name = gt.css('h3 a::text').extract_first().strip(), 
                    update_time = gt.css('relative-time ::attr(datetime)'
                            ).extract_first()
            )
            hub_url = response.css('h3 a::attr(href)').extract_first()
            full_hub_url = response.urljoin(hub_url)
            request = scrapy.Request(full_hub_url,self.parse_haha)
            request.meta['item'] = item
            print(item['name'])
            yield request

        #for url in response.css('div.paginate-container a::attr(href)').extract():
        #    yield response.follow(url, callback=self.parse)

    def parse_haha(self,response):
        item = response.meta['item']
        print('-------------------------------------------', item['name'])
        item['commits'] = response.css('li.commits span::text').extract_first().strip()
        item['branches'] = response.css('li span.num::text').extract()[1]
        item['releases'] = response.css('li span.num::text').extract()[2]
        return item
