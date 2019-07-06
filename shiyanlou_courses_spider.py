import scrapy

class shiyanlou_courses_spider(scrapy.Spider):
    name = 'shiyanlou_courses_spider'
    url_list = [
            'https://github.com/shiyanlou?before=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODowNjoxMSswODowMM4FkpTJ&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODowNjo1MyswODowMM4FkpKN&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0zMVQyMDoyMDowMiswODowMM4BzHi1&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wNFQwMDoxNzo1MyswODowMM4BpCnu&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0wOS0xNlQxMDowNjowMyswODowMM4Bb3Ud&tab=repositories'
            ]

    def parse(self,response):
        github = response.css('li.col-12')
        for g in github:
            yield {
                    'name':g.css('a::text').extract_first().strip(),
                    'updata_time':g.css('relative-time::text').extract_first()
                    }


