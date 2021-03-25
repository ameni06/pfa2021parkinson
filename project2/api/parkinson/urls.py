from django.conf.urls import url 
from parkinson import views 
 
urlpatterns = [ 
    url(r'^api/parkinson$', views.parkinson_list),
    url(r'^api/parkinson/(?P<pk>[0-9]+)$', views.parkinson_detail),
    url(r'^api/parkinson$', views.parkinson_list)
]