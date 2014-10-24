#
# episode.py
# Models that describe the underlying Episode data
#

import json


class Subtitle(object):
    """
    Model for a subtitle within an act
    """

    def __init__(self, role='', speaker='', time=0.0, paragraph=''):
        """
        Initialize Subtitle model
        :param role: Role of speaker (e.g. 'Host', 'Subject')
        :param speaker: Name of speaker
        :param time: Time in seconds since beginning
        :param paragraph: The words spoken
        """
        self.role = role
        self.speaker = speaker
        self.time = time
        self.paragraph = paragraph

    def to_dict(self):
        """
        Convert model to json-safe dict
        :return: JSON-safe dict
        """
        return self.__dict__


class Act(object):
    """
    Model for an act within a transcript
    """

    def __init__(self, act_title='', act_count=0, language='en-US', subtitles=[]):
        """
        Initialize Act model
        :param act_title: Title of act
        :param act_count: Act order in transcript
        :param language: ISO language code for act
        :param subtitles: List of subtitle objects in act
        """
        self.act_title = act_title
        self.act_count = act_count
        self.language = language
        self.subtitles = subtitles

    def to_dict(self):
        """
        Convert model to json-safe dict
        :return: JSON-safe dict
        """
        act_dict = dict()
        act_dict['act_title'] = self.act_title
        act_dict['act_count'] = self.act_count
        act_dict['language'] = self.language
        act_dict['subtitles'] = []
        for subtitle in self.subtitles:
            subtitle_dict = subtitle.to_dict()
            act_dict['subtitles'].append(subtitle_dict)

        return act_dict


class Transcript(object):
    """
    Model for a transcript in an episode of This American Life
    """

    def __init__(self, language='en-US', acts=[]):
        """
        Initialize Transcript model
        :param language: ISO language code for language
        :param acts: List of Act objects in transcript
        """
        self.language = language
        self.acts = acts

    def to_dict(self):
        """
        Convert model to json-safe dict
        :return: JSON-safe dict
        """
        transcript_dict = dict()
        transcript_dict['language'] = self.language
        transcript_dict['acts'] = []
        for act in self.acts:
            act_dict = act.to_dict()
            transcript_dict['acts'].append(act_dict)
        return transcript_dict


class Episode(object):
    """
    Model for an episode of This American Life
    """

    def __init__(self, number=None, title='', date=None, act_count=0, acts=[], languages=[], transcripts=[], audio=''):
        """
        Initialize Episode model
        :param number: Episode number
        :param title: Episode title
        :param date: Episode original air date
        :param act_count: Number of acts in episode
        :param acts: List of act names (e.g. 'Prologue', 'Act One')
        :param languages: List of supported language codes
        :param transcripts: List of Transcript objects for each supported language
        :param audio: URL of mp3
        """
        self.number = number
        self.title = title
        self.date = date
        self.act_count = act_count
        self.acts = acts
        self.languages = languages
        self.transcripts = transcripts
        self.audio = audio

    def to_json(self):
        """
        Convert model to json string and return
        :return: JSON string representation of Episode object
        """
        json_safe = dict()

        json_safe['number'] = self.number
        json_safe['title'] = self.title
        json_safe['date'] = self.date.strftime('%m.%d.%Y')
        json_safe['act_count'] = self.act_count
        json_safe['acts'] = self.acts
        json_safe['languages'] = self.languages
        json_safe['audio'] = self.audio

        json_safe['transcripts'] = []
        for transcript in self.transcripts:
            transcript_dict = transcript.to_dict()
            json_safe['transcripts'].append(transcript_dict)

        return json.dumps(json_safe)
