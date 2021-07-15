from django.conf.urls import url
 
# from . import views, testdb
from . import views
 
urlpatterns = [
    url('list', views.get_list),
    url('detail', views.get_detail),
    url('banner', views.get_banner)
]