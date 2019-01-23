from django.core.serializers import serialize
from django.http import HttpResponse
import json


class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        final_json = json.dumps(final_list)
        return final_json

class HttpResponseMixin(object):
    def render_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json', status=status)

