import datetime
import queue
import requests
from sortedcontainers import SortedKeyList


class CacheLRU:
    def __init__(self, max_cache_size, nodes_url, nodes_endpoints):
        self.memmory = dict()
        self.max_cache_size = max_cache_size
        self.usage_queue = queue.Queue()
        self.sorted_expiration_time_list = SortedKeyList(
            key=lambda item: item.expiration_datetime
        )
        self.nodes_url = nodes_url
        self.nodes_endpoints = nodes_endpoints

    def add_resource_to_cache(
        self,
        resource_id,
        resource_value,
        expires_in_seconds=100,
        curr_date=datetime.datetime.now(),
    ):
        if(not self.contains_cached_resource(resource_id) and self._is_memmory_full()):
            self._free_space()
        expiration_datetime = curr_date + \
            datetime.timedelta(seconds=expires_in_seconds)
        self.memmory[resource_id] = Resource(
            resource_id, resource_value, expiration_datetime
        )
        return True

    def find_resource(self, resource_id):
        # TODO check if is expired
        if(self.contains_cached_resource(resource_id)):
            return self.memmory[resource_id]
        else:
            return None

    def delete_resource_from_cache(self, resource_id):
        if self.contains_cached_resource(resource_id):
            # TODO delete from Queue and SortedKeyList also
            del self.memmory[resource_id]

    def contains_cached_resource(self, resource_id):
        return resource_id in self.memmory

    def _is_memmory_full(self):
        return self.max_cache_size == len(self.memmory)

    def _free_space(self, itens=1):
        resource_id = ''  # TODO find out which one should be deleted
        self.delete_resource(resource_id)

    def _delete_resources_by_cache_limit(self, resource_id):
        self.delete_resource(resource_id)

    def _delete_resources_by_expiration_time(self):
        self.sorted_expiration_time_list[0]

    def _notify_nodes(self, resource_id, resource_value):
        for node_url in self.nodes_url:
            url = node_url + self.nodes_endpoints["insert"]
            requests.post(f"{url}/{resource_id}", data=resource_value)


class Resource:
    def __init__(self, identifier, value, expiration_datetime):
        self.identifier = identifier
        self.value = value
        self.expiration_datetime = expiration_datetime
