from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^renderindex/', views.render_index, name='renderindex'),
	url(r'^index/', views.index, name='index'),
	url(r'^hello/v=(\d+)/', views.hello, name='hello')
]