from django.conf.urls import url
from . import views
 
app_name = 'entries'
 
urlpatterns = [
    url(r'^one$', views.one, name='one'),
]
