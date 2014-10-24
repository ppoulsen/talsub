#
# episode_spider.py
# The module which holds EpisodeSpider, the spider that crawls TAL episode transcripts
#

import datetime
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request

from items import *


class EpisodeSpider(scrapy.Spider):
    name = "episode"
    allowed_domains = ["thisamericanlife.org"]
    # URLs come from the start_requests() function
    start_urls = []
    # Format for TAL transcript HTML pages
    URL_FORMAT = 'http://www.thisamericanlife.org/radio-archives/episode/{0}/transcript'
    # Format for TAL mp3 locations
    MP3_URL_FORMAT = 'http://audio.thisamericanlife.org/jomamashouse/ismymamashouse/{0}.mp3'

    def __init__(self, start=1, stop=538):
        """
        Instantiate the EpisodeSpider
        :param start: Episode to start on (inclusive, first episode is 1)
        :param stop: Episode to end on (inclusive)
        """
        self.start = start
        self.stop = stop

    def start_requests(self):
        """
        This method is called by Scrapy before running. It yields requests
        to be scraped.

        :return: List of Item/Requests
        """

        cls = EpisodeSpider

        # Populate the request queue with every episode's transcript from start to stop
        for i in range(self.start, self.stop + 1):
            yield Request(cls.URL_FORMAT.format(i))

    def parse(self, response):
        """
        Parse the HttpResponse to an EpisodeItem and return.
        :param response: HttpResponse from a TAL transcript page
        :return: The parsed EpisodeItem
        """
        cls = EpisodeSpider

        item = EpisodeItem()
        selector = Selector(response=response)

        # Get episode number from div with class="radio-episode-num" and remove last character b/c it's a colon
        item['number'] = int(selector.xpath('//div[@class="radio-episode-num"]/text()').extract()[0][:-1])

        # Get title from the a tag in the only h2 tag in dev with class="radio"
        item['title'] = selector.xpath('//div[@class="radio"]/h2/a/text()').extract()[0]

        # Get data from dive with radio-date tag
        # The text is in the form "Originally Aired 11.17.1995", which is why we take the last word on ' ' split
        str_date = selector.xpath('//div[@class="radio-date"]/text()').extract()[0].split(' ')[-1]
        split_date = str_date.split('.')
        item['date'] = datetime.datetime(int(split_date[2]), int(split_date[0]), int(split_date[1]))

        # Take length of .act divs
        item['act_count'] = len(selector.xpath('//div[@class="act"]').extract())

        # The only h3 in each .act div is the title of the act
        item['acts'] = selector.xpath('//div[@class="act"]/h3/text()').extract()

        # All shows are in en-US
        item['languages'] = ['en-US']

        # All audio follows this format
        item['audio'] = cls.MP3_URL_FORMAT.format(item['number'])

        # Get Transcript
        item['transcripts'] = []
        item['transcripts'].append(self.parse_transcript(selector))

        return item

    def parse_transcript(self, selector):
        """
        Parse out the TranscriptItem from a Selector for the whole TAL transcript page
        :param selector: Selector object for xpath queries
        :return: TranscriptItem for page
        """
        item = TranscriptItem()

        # All shows are en-US
        item['language'] = 'en-US'

        # Parse acts
        index = 0
        item['acts'] = []
        acts = selector.xpath('//div[@class="act"]').extract()
        for act in acts:
            item['acts'].append(self.parse_act(Selector(text=act), index))
            index += 1

        return item

    def parse_act(self, selector, index):
        """
        Parse out the ActItem for a given Selector wrapping the <div class="act"> tag.
        :param selector: Selector for the <div class="act"> tag
        :param index: Index of the act on the page
        :return: ActItem for the div
        """
        item = ActItem()

        # Get act_title as with the list in EpisodeItem
        item['act_title'] = selector.xpath('//h3/text()').extract()[0]

        # Set to whatever was passed in
        item['act_count'] = index

        # All shows are en-US
        item['language'] = 'en-US'

        # Get subtitles
        item['subtitles'] = []
        subtitles = selector.xpath('//div[@class="act-inner"]/div').extract()
        for subtitle in subtitles:
            # Use extend, as subtitle may have multiple and thus parse_subtitles returns a list
            sub_selector = Selector(text=subtitle)
            new_subs = self.parse_subtitles(sub_selector)
            item['subtitles'].extend(new_subs)

        return item

    def parse_subtitles(self, selector):
        """
        Parse out the SubtitleItem(s) for a Selector wrapping the children div tags of <div class="act-inner">
        :param selector: Selector wrapping the children div tags of <div class="act-inner">
        :return: A list of SubtitleItems
        """

        # Initialize list for items
        items = []

        # Get role from top div's class attribute
        role = selector.xpath('/html/body/div/@class').extract()[0]

        # Set speaker to role by default, since some of these tags don't identify speaker
        speaker = role

        # Attempt to get the speaker's name from the h4 tag. If it exists, set speaker to that.
        potential_speaker = selector.xpath('/html/body/div/h4/text()').extract()
        if len(potential_speaker) > 0:
            speaker = potential_speaker[0]

        # Iterate through <p> tags for each SubtitleItem
        paragraphs = selector.xpath('/html/body/div/p').extract()
        for paragraph in paragraphs:
            # Item for each
            item = SubtitleItem()

            # Set the common role/speaker from above
            item['role'] = role
            item['speaker'] = speaker

            # New selector
            para_selector = Selector(text=paragraph)

            # Get time since
            time_str = para_selector.xpath('//p/@begin').extract()[0]
            # We're storing time in a float of seconds, so conver from HH:MM:SS.xx
            time_str_split = time_str.split(':')
            seconds = float(time_str_split[2])  # seconds
            seconds += float(time_str_split[1]) * 60.0  # minutes
            seconds += float(time_str_split[0]) * 60.0 * 60.0  # hours
            item['time'] = seconds

            # Append all text node descendants of <p> to erase HTML tags
            item['paragraph'] = ''.join(para_selector.xpath('//p//text()').extract())
            items.append(item)

        return items
