from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.course),
    url(r'^(?P<id>\d+)/delete$', views.delete),
]
