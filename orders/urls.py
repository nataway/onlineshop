
from django.conf.urls import url
from django.urls import path
from . import views
app_name='orders'

urlpatterns = [
    url(r'^my_order$', views.my_order, name='my_order'),
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^process/$', views.order_save, name='order_save'),
    path('(?P<id>\d+)/order_detail/$',views.order_detail, name='order_detail'),

]
