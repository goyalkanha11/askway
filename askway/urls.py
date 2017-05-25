
from django.conf.urls import url

from . import views

app_name='askway'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^log/$', views.log, name='log'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/postques$', views.post_ques, name='post_ques'),
    url(r'^home/postquestion$', views.post_question, name='post_question'),
    url(r'^home/(?P<question_id>[0-9]+)/answer$', views.answer, name='answer'),
    ]