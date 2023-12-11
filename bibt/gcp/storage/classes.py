import logging

from google.cloud import storage

_LOGGER = logging.getLogger(__name__)


class Client:
    """ """

    def __init__(self, credentials=None):
        self._client = storage.Client(credentials=credentials)
