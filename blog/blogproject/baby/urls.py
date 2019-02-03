from django.conf.urls import url
from . import views

app_name = 'baby'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^baby/', views.baby, name='detail'),
    url(r'^babyauto/', views.autodetail, name='detail'),
]

