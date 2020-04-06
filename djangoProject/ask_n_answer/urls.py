from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name='ask_n_answer.hello'),
    url(r'^$', views.index, name='ask_n_answer.index'),
    url(r'^hot/', views.hot, name='ask_n_answer.hot'),
    url(r'^tag/(?P<tag>\w+)/$', views.tag, name='ask_n_answer.tag'),
    url(r'^question/(?P<id>\d+)/$', views.question, name='ask_n_answer.question'),
    url(r'^login/', views.login, name='ask_n_answer.login'),
    url(r'^signup/', views.signup, name='ask_n_answer.signup'),
    url(r'^ask/', views.ask, name='ask_n_answer.ask'),
]
