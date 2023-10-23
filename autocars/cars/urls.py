from django.conf.urls import url
from .import views

urlpatterns = [
    url('^cars/$', views.CarList.as_view(), name='car-list'),

]