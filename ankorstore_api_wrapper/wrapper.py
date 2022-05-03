import json

import requests as rq

from ankorstore_api_wrapper import utils, resources


class APIWrapper:
    BASE_URL = 'https://www.ankorstore.com'
    BASE_URL_SANDBOX = 'https://www.public.sandbox.ankorstore.com'

    def __init__(self, api_version, client_id, client_secret, sandbox=False):
        self._api_version = api_version
        self._client_id = client_id
        self._client_secret = client_secret

        self._base_url = self.BASE_URL if not sandbox else self.BASE_URL_SANDBOX
        self._base_host = utils.urljoin(self._base_url, 'api', self._api_version)
        self._session = rq.Session()

        self._resources = {
            'orders': resources.OrderPool(
                utils.urljoin(self._base_host, 'orders'), self._session),
        }

    @property
    def resources(self):
        """Return all resources as a list of Resources"""
        return self._resources

    @property
    def orders(self):
        return self._resources['orders']

