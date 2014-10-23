#
# episode.py
# Models that describe the underlying Episode data
#


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


class Episode(object):
    """
    Model for an episode of This American Life
    """

    def __init__(self, number, title='', date=None, act_count=0, acts=[], languages=[], transcripts=[], audio=''):
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
