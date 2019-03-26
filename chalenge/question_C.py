import datetime
import queue
from sortedcontainers import SortedKeyList


class CacheLRU:
    def __init__(self, cache_size):
        self.memmory = dict()
        self.usage_queue = queue.Queue(max_size=cache_size)
        self.sorted_expiration_time_list = SortedKeyList(
            key=lambda item: item.expiration_datetime
        )

    def contains_cached_resource(self, resource_id):
        return resource_id in self.memmory

    def delete_resources_by_cache_limit(self, resource_id):
        self.delete_resource(resource_id)

    def delete_resources_by_expiration_time(self):
        self.sorted_expiration_time_list[0]

    def delete_resource(self, resource_id):
        if self.contains_cached_resource(resource_id):
            del self.memmory[resource_id]

    def notify_nodes():
        # TODO
        all_nodes = ()
        for n in all_nodes:
            print(n)

    def cache_resource(
        self,
        resource_id,
        resource_value,
        expires_in_seconds=100,
        curr_date=datetime.now,
    ):
        expiration_datetime = curr_date + datetime.timedelta(seconds=expires_in_seconds)
        self.memmory[resource_id] = Resource(
            resource_id, resource_value, expiration_datetime
        )
        return True


class Resource:
    def __init__(self, identifier, value, expiration_datetime):
        self.identifier = identifier
        self.value = value
        self.expiration_datetime = expiration_datetime
