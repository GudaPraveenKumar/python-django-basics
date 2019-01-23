from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
from testapp.mixins import HttpResponseMixin


def emp_data_view(request):

    emp_data={
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai'
    }
    resp = '<h2>Employee Number: {}<br> Name: {}<br> Salary:{}<br> Address: {}</h2>'.format(emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddr'])
    return HttpResponse(resp)


def emp_data_jsonview(request):

    emp_data={
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai'
    }
    json_data = json.dumps(emp_data)

    return HttpResponse(json_data, content_type='application/json')


def emp_data_jsonview2(request):

    emp_data={
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai'
    }
    # json_data = json.dumps(emp_data)

    return JsonResponse(emp_data, content_type='application/json')


class JsonCBV(HttpResponseMixin, View):

    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from GET method'})
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from POST method'})
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from PUT method'})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from DELETE method'})
        return self.render_to_http_response(json_data)


