from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name='blog.hello'),
    url(r'^$', views.index, name='blog.index'),
    url(r'^hot/', views.hot, name='blog.hot'),
    url(r'^tag/(?P<tag>\w+)/$', views.tag, name='blog.tag'),
    url(r'^question/(?P<id>\d+)/$', views.question, name='blog.question'),
    url(r'^login/', views.login, name='blog.login'),
    url(r'^signup/', views.signup, name='blog.signup'),
    url(r'^ask/', views.ask, name='blog.ask'),
]
