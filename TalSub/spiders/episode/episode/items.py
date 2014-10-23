# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubtitleItem(scrapy.Item):
    role = scrapy.Item()
    speaker = scrapy.Item()
    time = scrapy.Item()
    paragraph = scrapy.Item()


class ActItem(scrapy.Item):
    act_title = scrapy.Item()
    act_count = scrapy.Item()
    language = scrapy.Item()
    subtitles = scrapy.Item()


class TranscriptItem(scrapy.Item):
    language = scrapy.Item()
    acts = scrapy.Item()


class EpisodeItem(scrapy.Item):
    number = scrapy.Item()
    title = scrapy.Item()
    date = scrapy.Item()
    act_count = scrapy.Item()
    acts = scrapy.Item()
    languages = scrapy.Item()
    transcripts = scrapy.Item()
    audio = scrapy.Item()
