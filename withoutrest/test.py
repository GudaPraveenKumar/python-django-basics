import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsoncbv/'
resp = requests.get(BASE_URL+ENDPOINT)
data = resp.json()
print(data)


# print(type(resp))
# print(type(resp.json()))
# print(resp.json())
#
# data = resp.json()
#
# print('Employee Number:', data['eno'])
# print('Employee Name:', data['ename'])
# print('Employee Salary:', data['esal'])
# print('Employee Address:', data['eaddr'])


def f1(*args):
    # *args convert all arguments to tuples
    print(args)


f1()
f1(10)
f1(10, 20)


def f2(**kwargs):
    # **kwargs converts all arguments to dictionary
    print(kwargs)


f2(name='debba', rollno='20', marks=90, address='asdf')