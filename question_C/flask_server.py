from flask import Flask, request, abort, Response
from flask_restplus import Api, Resource, fields
from .CacheLRU import CacheLRU
import datetime


app = Flask(__name__)

api = Api(app, version='1.0', title='LRU cache with time expiration',
          description='LRU cache with time expiration'
          )


nodes_url = ["http://localhost:5000"]
expiration_seconds = 3
max_cache_size = 100

nodes_endpoints = {
    "insert": "/add_resource_to_cache",
    "find": "/find_resource_in_cache",
    "used": "/resource_used_in_cache"
}

cache = CacheLRU(max_cache_size, nodes_url, nodes_endpoints)


@api.route(f"{nodes_endpoints['insert']}/<resource_id>", methods=['POST'])
@api.doc(params={'resource_id': 'Resource identifier'})
class AddResourceToCache(Resource):
    @api.expect(api.model('Any object', ""))
    def post(self, resource_id):
        try:
            notify_nodes = request.args.get(
                "notify_nodes", default=True) is True
            expiration_datetime_str = request.args.get(
                "expiration_datetime")
            expiration_datetime = datetime.datetime.fromisoformat(
                expiration_datetime_str) \
                if expiration_datetime_str is not None \
                else self.calculate_expiration_seconds()

            cache.add_resource_to_cache(resource_id,
                                        request.get_data(),
                                        request.content_type,
                                        notify_nodes,
                                        expiration_datetime)
            return '', 201
        except Exception as e:
            return f'Unknown error: {e}', 500

    def calculate_expiration_seconds(self):
        return datetime.datetime.now() \
            + datetime.timedelta(seconds=expiration_seconds)


@api.route(f"{nodes_endpoints['find']}/<resource_id>", methods=['GET'])
@api.doc(params={'resource_id': 'Resource identifier'})
class FindResourceInCache(Resource):
    def get(self, resource_id):
        resource, mimetype = cache.find_resource(resource_id)
        if(resource is None):
            return '', 404
        else:
            return Response(resource, mimetype=mimetype)


@api.route(f"{nodes_endpoints['used']}/<resource_id>", methods=['POST'])
@api.doc(params={'resource_id': 'Resource identifier'})
class ResourceUsedInCache(Resource):
    def post(self, resource_id):
        cache.resource_used_in_cache(resource_id, False)
        return '', 202
