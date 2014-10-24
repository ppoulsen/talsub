#
# run.py
# Simple script for running the spider.
#

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings

from spiders.episode_spider import EpisodeSpider

# TODO: Add argparse so developers don't need to edit this file when running a job
if __name__ == '__main__':
    # Instantiate spider
    # NOTE: Change EpisodeSpider constructor args to limit scope
    # e.g. EpisodeSpider(start=10, end=12) will crawl TAL episodes 10, 11, and 12
    spider = EpisodeSpider()

    # Get settings from settings.py
    settings = get_project_settings()

    # Instantiate Crawler
    crawler = Crawler(settings)

    # Run crawler with EpisodeSpider
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    reactor.run()