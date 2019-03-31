=========================================================
Question C
=========================================================
Write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

1 - Simplicity. Integration needs to be dead simple.

2 - Resilient to network failures or crashes.

3 - Near real time replication of data across Geolocation. Writes need to be in real time.

4 - Data consistency across regions

5 - Locality of reference, data should almost always be available from the closest region

6 - Flexible Schema

7 - Cache can expire



### Implementation

The cache implementation that I've tried to do has the following behaviour:

The cache mechanism is the same in all nodes. 
It has 3 endpoints: 

1)POST add_resource_to_cache/{resource_id}?notify_nodes=(true|false)&expires_at=2019-01-01T00:00:00.000-05:00
Used to store/update value of a resource in cache.
It can be called from an application or from other nodes:
If called from an application, it should notify all other nodes to update their cache as well.
If called from other noded, it should update their value only.

2)GET find_resource_in_cache/{resource_id}
Used by applications as first try of finding resource. 
If resource is not cached, it will return HTTP status 404, which will make application get the resource and add it to the cache.
If resource is cached, it will return HTTP status 200 with the resource.

3)POST resource_used_in_cache/{resource_id}
Used to a note notify other nodes that a resource was recentlly used, and should update its place at LRU queue.


To implement this behaviour, a machine like the proxy server, or the gateway should intercept requests, and query them on this application dealing with the error status.
Whenever a resource coud't be found at cache, the original request should be done, adding the value to the cache after.

===================
Future improvements 
===================
Impelemnt some kind of service discovery or other tool that allows all nodes to notify a single service, that broadcasts the message to all the others.
Implement periodically service that removes expired resources from memmory