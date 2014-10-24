# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubtitleItem(scrapy.Item):
    role = scrapy.Field()
    speaker = scrapy.Field()
    time = scrapy.Field()
    paragraph = scrapy.Field()


class ActItem(scrapy.Item):
    act_title = scrapy.Field()
    act_count = scrapy.Field()
    language = scrapy.Field()
    subtitles = scrapy.Field()


class TranscriptItem(scrapy.Item):
    language = scrapy.Field()
    acts = scrapy.Field()


class EpisodeItem(scrapy.Item):
    number = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    act_count = scrapy.Field()
    acts = scrapy.Field()
    languages = scrapy.Field()
    transcripts = scrapy.Field()
    audio = scrapy.Field()
