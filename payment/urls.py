from django.urls import path
from django.conf.urls import url


from payment import views

app_name = 'payment'
urlpatterns = [

    # path('canceled/$', views.payment_canceled, name='canceled'),
    # path('done/$', views.payment_done, name='done'),
    # path('(?P<id>\d+)/process', views.payment_process, name='process'),
    path('review', views.add_review, name='review_product'),
    path('addReview/(?P<id_product>\d+)/$',views.add_review, name="addreview"),
    url(r'^review/$', views.add_review, name='review_product'),
]
