from django.contrib import admin
from testapp.models import Employee, User

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(User, UserAdmin)
