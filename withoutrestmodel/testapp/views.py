from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee, User
from django.http import HttpResponse
from testapp.mixins import SerializeMixin, HttpResponseMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(SerializeMixin, HttpResponseMixin, View):

    def get_object_by_id(self, resource_id):
        try:
            emp = Employee.objects.get(id = resource_id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide valid json data'})
            return self.render_http_response(json_data, status=400)
        pdata = json.loads(data)
        resource_id = pdata.get('id', None)
        if resource_id is not None:
            emp = self.get_object_by_id(resource_id)
            if emp is None:
                json_data = json.dumps({'msg': 'Requested emp not found with provided id'})
                return self.render_http_response(json_data, status=404)
            json_data= self.serialize([emp, ])
            return self.render_http_response(json_data)
        emp_list = Employee.objects.all()
        json_data = self.serialize(emp_list)
        return self.render_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)

        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid json data'})
            return self.render_http_response(json_data, status=400)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource Created Successfully'})
            return self.render_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide valid json data'})
            return self.render_http_response(json_data, status=400)
        pdata = json.loads(data)
        resource_id = pdata.get('id', None)
        if resource_id is None:
            json_data = json.dumps({'msg': 'Id is required for updating'})
            return self.render_http_response(json_data, status=404)
        emp = self.get_object_by_id(resource_id)
        if emp is None:
            json_data = json.dumps({'msg': 'Emp not found with this id'})
            return self.render_http_response(json_data, status=404)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr,
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource Updated Successfully'})
            return self.render_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailsCBV(SerializeMixin, HttpResponseMixin, View):

    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The Employee not found'})
            return self.render_http_response(json_data, status=404)
        else:
            json_data = self.serialize([emp, ])
            return self.render_http_response(json_data)

    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'Employee not found Not Possible to perform updation'})
            return self.render_http_response(json_data, status=404)

        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send valid json data'})
            return self.render_http_response(json_data, status=400)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr,
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource Updated Successfully'})
            return self.render_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)

    def delete(self, request,id, *args, **kwargs):
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'Employee not found Not Possible to perform delete'})
                return self.render_http_response(json_data, status=404)
            t = emp.delete()
            status, deleted_item = t
            print(status, deleted_item)
            json_data = json.dumps({'msg': 'Resource Deleted Successfully'})
            return self.render_http_response(json_data)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(SerializeMixin, HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)

        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid json data'})
            return self.render_http_response(json_data, status=400)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource Created Successfully'})
            return self.render_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_http_response(json_data, status=400)
