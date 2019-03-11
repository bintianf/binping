from django.conf.urls import url
from . import views

app_name = 'baby'
urlpatterns = [
    url(r'^$', views.babyindex, name='babyindex'),
    # url(r'^babyauto/', views.autodetail, name='autodetail'),
    url(r'^age/(?P<pk>[0-9]+)/$', views.age, name='age'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group, name='group')
]

