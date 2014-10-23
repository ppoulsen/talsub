#
# dto.py
# This module defines the DTOs used to communicate with the db
#

import mongoengine as me


class SubtitleDTO(me.EmbeddedDocumentField):
    """
    A sub-DTO to encapsulate a single subtitle of an act. Use by ActDTO
    """

    # Roles such as host, subject, and interviewer
    role = me.StringField(db_field='r')
    speaker = me.StringField(db_field='s')
    # Seconds since beginning of audio
    time = me.FloatField(db_field='t', min_value=0.0)
    paragraph = me.StringField(db_field='p')


class ActDTO(me.EmbeddedDocumentField):
    """
    A sub-DTO to encapsulate an act of a transcript. Used by TranscriptDTO.
    """

    act_title = me.StringField(db_field='t')
    act_count = me.IntField(db_field='c', min_value=0)
    language = me.StringField(db_field='l')
    subtitles = me.ListField(db_field='s', field=me.EmbeddedDocumentField(SubtitleDTO))


class TranscriptDTO(me.EmbeddedDocument):
    """
    A sub-DTO to encapsulate transcripts. Used by EpisodeDTO.
    """

    language = me.StringField(db_field='l')
    acts = me.ListField(db_field='a', field=me.EmbeddedDocumentField(ActDTO))


class EpisodeDTO(me.Document):
    """
    A DTO for Episode documents.
    """

    number = me.IntField(db_field='n', min_value=1, required=True, unique=True, primary_key=True)
    title = me.StringField(db_field='t')
    date = me.DateTimeField(db_field='d')
    act_count = me.IntField(db_field='ac', min_value=1)
    acts = me.ListField(db_field='a', field=me.StringField())
    languages = me.ListField(db_field='l', field=me.StringField())
    transcripts = me.ListField(db_field='t', field=me.EmbeddedDocumentField(TranscriptDTO))
    audio = me.URLField(db_field='au')
