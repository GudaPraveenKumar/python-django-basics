import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


def get_resource_single_api(resource_id=None):
    data = {}
    if resource_id is not None:
        data = {
            'id': resource_id
        }
    resp = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


def get_all_resource():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())


def get_resource(resource_id):
    resp = requests.get(BASE_URL+ENDPOINT+resource_id+'/')
    print(resp.status_code)
    if resp.status_code in range(200, 300):
        # if resp.status_code == requests.codes.ok:
        print(resp.json())
    else:
        print('Something went wrong')
        print(resp.json())


def create_resource():
    new_emp = {
        'eno': 550,
        'ename': 'Raju',
        'esal': 5000,
        'eaddr': 'Delhi',
    }
    resp = requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


def update_resource(resource_id):
    new_emp = {
        'ename': 'Rahul',
        'esal': 10000,
        'eaddr': 'Chilkanagar',
    }
    resp = requests.put(BASE_URL + ENDPOINT + str(resource_id) + '/', data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

def update_resource_single_api(resource_id):
    new_emp = {
        'id':resource_id,
        'ename': 'Charan',
        'esal': 8500,
        'eaddr': 'Shamirpet',
    }
    resp = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


def delete_resource(resource_id):
    resp = requests.delete(BASE_URL + ENDPOINT + str(resource_id) + '/')
    print(resp.status_code)
    print(resp.json())


def delete_resource_single_api(resource_id):
    data = {
        'id': resource_id
    }
    resp = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


delete_resource_single_api(4)
# update_resource_single_api(3)
# get_resource_single_api(2)
# delete_resource(2)
# update_resource(2)
# create_resource()
# id = input('Enter some id = ')
# get_resource(id)
# get_all_resource()
