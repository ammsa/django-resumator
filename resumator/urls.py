from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.about, name='index'),
    url(r'^about/$', views.about, name='index'),
    url(r'^projects/$', views.projects, name='index'),
    url(r'^experience/$', views.experience, name='index'),
    url(r'^publications/$', views.publications, name='index'),
    url(r'^education/$', views.education, name='index'),
]
