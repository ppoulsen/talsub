#
# dao.py
# This module regulates the use of DTOs through data access objects.
#

from data.connection import DBConnection
from data.dto import EpisodeDTO


class DAO(object):
    """
    An abstract DAO class
    """

    def __init__(self):
        self.conn = DBConnection

    def all(self, *only):
        """
        Returns all documents in the collection.

        :param only: Only return these fields from collection
        :return: The document with specified fields
        """
        with self.conn():
            return self.dto.objects().only(*only)

    def find(self, *only, **constraints):
        """
        Returns all documents that match constraints.

        :param only: Only return these fields.
        :param constraints: Only return documents that match this criteria
        :return: A collection of documents that match criteria
        """
        with self.conn():
            return self.dto.objects(**constraints).only(*only)

    def insert(self, dto):
        """
        Insert/update dto in database.
        :param dto: The dto to insert/update
        :return: The dto
        """
        with self.conn():
            dto.save()
        return dto


class EpisodeDAO(DAO):
    """
    A DAO class for Episode DTOs
    """

    def __init__(self):
        super(EpisodeDAO, self).__init__()
        self.dto = EpisodeDTO