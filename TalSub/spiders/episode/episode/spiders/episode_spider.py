import scrapy
from scrapy.http import Request


class EpisodeSpider(scrapy.Spider):
    name = "episode"
    allowed_domains = ["thisamericanlife.org"]
    start_urls = [ ]
    URL_FORMAT='http://www.thisamericanlife.org/radio-archives/episode/{0}/transcript'

    def __init__(self, start=1, stop=538):
        self.start = start
        self.stop = stop

    def start_requests(self):
        """
        This method is called by Scrapy before running. It yields requests
        to be scraped.

        :return: List of Item/Requests
        """

        cls = EpisodeSpider

        for i in range(self.start, self.stop):
            yield Request(cls.URL_FORMAT.format(i))

    def parse(self, response):
        pass
