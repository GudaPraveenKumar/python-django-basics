
from django.conf.urls import url
from . import views

app_name = "book"

# Generic view
urlpatterns = [
    url(r'^$', views.EmployeeCRUDCBV.as_view(), name="list"),
    url(r'^(?P<id>\d+)/$', views.EmployeeDetailsCBV.as_view(), name="details"),
]
