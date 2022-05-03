import json

from ankorstore_api_wrapper.utils import urljoin

class ResourcePool:
    def __init__(self, endpoint, session):
        """Initialize the ResourcePool to the given endpoint. Eg: products"""
        self._endpoint = endpoint
        self._session = session

    def get_url(self):
        return self._endpoint

class CreatableResource:
    def create_item(self, item):
        res = self._session.post(self._endpoint, data=json.dumps(item))
        return res

class GettableResource:
    def fetch_item(self, code, params=None):
        url = urljoin(self._endpoint, code)
        res = self._session.get(url, params=params)
        return res

class ListableResource:
    def fetch_list(self, params=None):
        res = self._session.get(self._endpoint, params=params)
        return res

class SearchableResource:
    def search(self, query):
        params = {
            'query': query
        }
        res = self._session.get(self._endpoint, params=params)
        return res

class UpdatableResource:
    def update_create_item(self, item, code=None):
        if code is None:
            code = item.get('id')
        url = urljoin(self._endpoint, code)
        res = self._session.put(url, data=json.dumps(item))
        return res

class DeletableResource:
    def delete_item(self, code):
        url = urljoin(self._endpoint, code)
        res = self._session.delete(url)
        return res