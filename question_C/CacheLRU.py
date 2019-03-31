import datetime
import requests
from sortedcontainers import SortedKeyList
from llist import dllist
import logging

logger = logging.getLogger('CacheLRU')
logger.setLevel(logging.DEBUG)


class CacheLRU:
    def __init__(self, max_cache_size, nodes_url,
                 nodes_endpoints):
        self.memmory = dict()
        self.max_cache_size = max_cache_size
        self.usage_list = dllist()
        self.sorted_expiration_time_list = SortedKeyList(
            key=lambda item: item.expiration_datetime
        )
        self.nodes_url = nodes_url
        self.nodes_endpoints = nodes_endpoints

    def add_resource_to_cache(
        self,
        resource_id,
        resource_value,
        notify_nodes,
        expiration_datetime,
    ):
        if(not self.contains_cached_resource(resource_id)):
            while(self._is_memmory_full()):
                self._free_space()
        else:
            self.usage_list.remove(resource_id)
        resource = Resource(
            resource_id, resource_value, expiration_datetime
        )
        self.memmory[resource_id] = resource
        self.sorted_expiration_time_list.add(resource)
        self.usage_list.appendleft(resource_id)
        if(notify_nodes):
            self._notify_nodes_add(
                resource_id, resource_value, expiration_datetime)

    def find_resource(self, resource_id):
        self._delete_resources_by_expiration_time()
        if(self.contains_cached_resource(resource_id)):
            self.update_usage_list(resource_id, True)
            resource_value = self.memmory[resource_id]
            return resource_value
        else:
            return None

    def update_usage_list(self, used_resource_id, notify_nodes):
        self.usage_list.remove(used_resource_id)
        self.usage_list.appendleft(used_resource_id)
        if notify_nodes:
            self._notify_nodes_used(used_resource_id)

    def delete_resource_from_cache(self, resource_id):
        if self.contains_cached_resource(resource_id):
            self.usage_list.remove(resource_id)
            self.sorted_expiration_time_list.remove(self.memmory[resource_id])
            del self.memmory[resource_id]

    def contains_cached_resource(self, resource_id):
        return resource_id in self.memmory

    def _is_memmory_full(self):
        return self.max_cache_size == len(self.memmory)

    def _free_space(self, itens=1):
        resource_id = self.usage_list.first.value
        self.delete_resource(resource_id)

    def _delete_resources_by_expiration_time(self, curr_date=datetime
                                             .datetime.now()):
        for resource in self.sorted_expiration_time_list:
            if resource.expiration_datetime <= curr_date:
                self.delete_resource_from_cache(resource.identifier)
            else:
                break

    def _notify_nodes_add(self,
                          resource_id,
                          resource_value,
                          expiration_datetime):
        for node_url in self.nodes_url:
            url = node_url + self.nodes_endpoints["insert"]
            payload = {'notify_nodes': False,
                       'expiration_datetime': expiration_datetime}
            requests.post(f"{url}/{resource_id}",
                          data=resource_value, params=payload)

    def _notify_nodes_used(self, resource_id, datetime_read):
        for node_url in self.nodes_url:
            url = node_url + self.nodes_endpoints["used"]
            payload = {'notify_nodes': False, 'datetime': datetime_read}
            requests.get(f"{url}/{resource_id}", params=payload)


class Resource:
    def __init__(self, identifier, value, expiration_datetime):
        self.identifier = identifier
        self.value = value
        self.expiration_datetime = expiration_datetime
