from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^$', views.find, name='find'),
    url(r'^results/$', views.find, name='find'),
]