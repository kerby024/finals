from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.display),
        url(r'^poker/(?P<pokedid>\d+)$', views.counter),
        url(r'^clear', views.clear),
]