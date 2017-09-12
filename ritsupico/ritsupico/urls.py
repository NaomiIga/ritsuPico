"""ritsupico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import include, url
from django.contrib import *
#from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
from django.conf import settings
from cms import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('django.contrib.staticfiles.urls')),
    url(r'^pico_login', views.pico_login, name="pico_login"),
    url(r'^hint', views.hint, name="hint"),
    url(r'^treasure_check', views.treasure_check, name="treasure_check"),
    url(r'^export_csv', views.export_csv, name="export_csv"),
    url(r'^finish', views.finish, name="finish"),
    url(r'^key_get', views.key_get, name="key_get"),
    url(r'^recover_check', views.recover_check, name="recover_check"),
    url(r'^recover_data', views.recover_data, name="recover_data"),
    url(r'^recover_data2', views.recover_data2, name="recover_data2")
]
