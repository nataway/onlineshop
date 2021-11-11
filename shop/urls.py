from django.urls import path
from shop import views
app_name='shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search', views.product_search, name='product_search'),
    path('(?P<category_slug>[-\w]+)/$',
        views.product_list, name='product_list_by_category'),
    path('(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail, name='product_detail'),
    path('send_mail/(?P<product_id>\d+)/$',views.share_post, name="send_mail"),

]