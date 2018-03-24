import scrapy

class RedditMessageSpider(scrapy.Spider):
    name = "message"
    
    def start_requests(self, url_string) :
        urls = [url_string,]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)






# EVERYTHING BELOW THIS IS A TEST #

red = RedditMessageSpider()
red.start_requests("http://quotes.toscrape.com/tag/humor/")

