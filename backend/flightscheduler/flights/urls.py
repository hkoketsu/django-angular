from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    url(r'^$', views.flight_list),
    url(r'^(?P<pk>[0-9]+)$', views.flight_detail)
]
