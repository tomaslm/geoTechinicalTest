from flask import Flask

# import sched
from .CacheLRU import CacheLRU


app = Flask(__name__)


nodes_url = ["http://localhost:5000"]

nodes_endpoints = {
    "insert": "add_resource_to_cache",
    "find": "find_resource_in_cache",
    "delete": "delete_resource_from_cache",
}

cache = CacheLRU(100, nodes_url, nodes_endpoints)


@app.route(f"{nodes_endpoints['insert']}/<resource_id>")
def add_resource_to_cache(resource_id, resource_value):
    cache.cache_resource(resource_id, resource_value)


@app.route(f"{nodes_endpoints['find']}/<resource_id>")
def find_resource_in_cache(resource_id):
    # TODO
    return "Hello, World!"


@app.route(f"{nodes_endpoints['delete']}/<resource_id>")
def delete_resource_from_cache(resource_id):
    # TODO
    return "Hello, World!"
