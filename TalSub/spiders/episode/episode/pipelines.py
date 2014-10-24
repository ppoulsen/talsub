# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from data.dao import EpisodeDAO
from data.dto import EpisodeDTO
from models.episode import Episode
from shared.converters import *


class EpisodePipeline(object):
    def process_item(self, item, spider):
        model = ModelConverter().to_model(Episode, item)
        dto = DTOConverter().to_dto(EpisodeDTO, model)
        dao = EpisodeDAO()
        dao.insert(dto)
