from django.conf.urls import url
from django.contrib import admin

# import views
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]

