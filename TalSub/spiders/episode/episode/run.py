#
# run.py
# Simple script for running the spider.
#

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from spiders.episode_spider import EpisodeSpider

# TODO: Add argparse so developers don't need to edit this file when running a job
if __name__ == '__main__':
    # Get settings from settings.py
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    # NOTE: Change EpisodeSpider constructor args to limit scope
    # e.g. EpisodeSpider(start=10, stop=12) will crawl TAL episodes 10, 11, and 12
    process.crawl(EpisodeSpider, start=1, stop=564)
    process.start() # the script will block here until the crawling is finished
