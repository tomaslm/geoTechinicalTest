from flask import Flask, request, abort

# import sched
from .CacheLRU import CacheLRU


app = Flask(__name__)


nodes_url = ["http://localhost:5000"]

nodes_endpoints = {
    "insert": "/add_resource_to_cache",
    "find": "/find_resource_in_cache",
    "delete": "/delete_resource_from_cache",
}

cache = CacheLRU(100, nodes_url, nodes_endpoints)


@app.route(f"{nodes_endpoints['insert']}/<resource_id>", methods=['POST'])
def add_resource_to_cache(resource_id):
    try:
        cache.add_resource_to_cache(resource_id, request.get_data())
        return '', 201
    except Exception as e:
        return f'Unknown error: {e}', 500


@app.route(f"{nodes_endpoints['find']}/<resource_id>", methods=['GET'])
def find_resource_in_cache(resource_id):
    resource = cache.find_resource(resource_id)
    if(resource is None):
        return '', 404
    else:
        return resource


@app.route(f"{nodes_endpoints['delete']}/<resource_id>", methods=['DELETE'])
def delete_resource_from_cache(resource_id):
    cache.delete_resource_from_cache(resource_id)
    return '', 204
