from flask import Flask, request, abort
from flask_restplus import Api, Resource, fields
from .CacheLRU import CacheLRU
import datetime


app = Flask(__name__)

api = Api(app, version='1.0', title='LRU cache with time expiration',
          description='LRU cache with time expiration'
          )


nodes_url = ["http://localhost:5000"]
expiration_seconds = 30
max_cache_size = 5

nodes_endpoints = {
    "insert": "/add_resource_to_cache",
    "find": "/find_resource_in_cache",
    "used": "/resource_used_in_cache"
}

cache = CacheLRU(max_cache_size, nodes_url, nodes_endpoints)


@api.route(f"{nodes_endpoints['insert']}/<resource_id>", methods=['POST'])
class AddResourceToCache(Resource):
    def post(self, resource_id):
        try:
            notify_nodes = request.args.get("notify_nodes", True)
            expiration_datetime = request.args.get(
                "expiration_datetime",
                self.calculate_expiration_seconds()
            )

            cache.add_resource_to_cache(resource_id, request.get_data(
            ), notify_nodes, expiration_datetime)
            return '', 201
        except Exception as e:
            return f'Unknown error: {e}', 500

    def calculate_expiration_seconds(self):
        return datetime.datetime.now() \
            + datetime.timedelta(seconds=expiration_seconds)


@api.route(f"{nodes_endpoints['find']}/<resource_id>", methods=['GET'])
class FindResourceInCache(Resource):
    def get(resource_id):
        resource = cache.find_resource(resource_id)
        if(resource is None):
            return '', 404
        else:
            return resource, 200


@api.route(f"{nodes_endpoints['used']}/<resource_id>", methods=['POST'])
class ResourceUsedInCache(Resource):
    def post(resource_id):
        cache.resource_used_in_cache(resource_id, False)
        return '', 202
