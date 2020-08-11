from django.conf.urls import include,url

from . import views
app_name = 'spfdetect'

urlpatterns = [
    url('', views.index, name='index'),
    url(r'^detect/', views.detect, name='detect'),
]
