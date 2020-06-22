from django.contrib import admin
from django.urls import path, re_path
from basic_app import views

#template tagging
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^rel_url_temp/$',views.relative,name='relative'),
    re_path(r'^other/$',views.other,name='other'),
]
