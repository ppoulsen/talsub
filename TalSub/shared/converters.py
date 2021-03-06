#
# converters.py
# A Module for converting from Model <-> DTO and ScrapyItem -> Model
#

from model.episode import *
from data.dto import *
from data.dao import *


class DTOConverter(object):
    """A class for converting base objects to and from DTOs."""

    @staticmethod
    def from_dto(cls, obj):
        """
        Returns the base object mapping of a DTO.

        :param cls: The class to convert to.
        :param obj: The object to convert.
        :return: Model of DTO
        """
        if obj is None:
            return None

        if not hasattr(obj, '_data'):
            return None

        new_model = cls()

        for key in obj._data:
            if key == 'transcripts':
                setattr(new_model, key, [DTOConverter.from_dto(Transcript, t) for t in obj._data[key]])
            elif key == 'acts' and cls == Transcript:
                setattr(new_model, key, [DTOConverter.from_dto(Act, a) for a in obj._data[key]])
            elif key == 'subtitles':
                setattr(new_model, key, [DTOConverter.from_dto(Subtitle, s) for s in obj._data[key]])
            else:
                if key != 'id':
                    setattr(new_model, key, obj._data[key])

        return new_model

    @staticmethod
    def to_dto(cls, obj):
        """
        Returns the DTO mapping of a base object.

        :param cls: The DTO class to convert to.
        :param obj: The object to convert.
        :return: The DTO representation of the base object.
        """
        new_dto = cls()

        # Grab DTO from db if exists
        if cls == EpisodeDTO:
            existing = EpisodeDAO().find(number=obj.number).first()
            if existing:
                new_dto = existing

        for key, value in obj.__dict__.iteritems():
            if key == 'transcripts':
                setattr(new_dto, key, [DTOConverter.to_dto(TranscriptDTO, t) for t in value])
            elif key == 'acts' and cls == TranscriptDTO:
                setattr(new_dto, key, [DTOConverter.to_dto(ActDTO, a) for a in value])
            elif key == 'subtitles':
                setattr(new_dto, key, [DTOConverter.to_dto(SubtitleDTO, s) for s in value])
            else:
                setattr(new_dto, key, value)

        return new_dto


class ModelConverter(object):
    """
    This class converts any dict-like object into a model based on member names.
    """

    @staticmethod
    def to_model(cls, obj):
        """
        Converts the obj to a model of type cls
        :param cls: The model class to convert to
        :param obj: The dict-like object to convert to cls
        :return: A model of type cls
        """

        new_model = cls()

        for key, value in obj.iteritems():
            if value:
                if key == 'transcripts':
                    setattr(new_model, key, [ModelConverter.to_model(Transcript, t) for t in value])
                elif key == 'acts' and cls == Transcript:
                    setattr(new_model, key, [ModelConverter.to_model(Act, a) for a in value])
                elif key == 'subtitles':
                    setattr(new_model, key, [ModelConverter.to_model(Subtitle, s) for s in value])
                else:
                    setattr(new_model, key, value)

        return new_model
