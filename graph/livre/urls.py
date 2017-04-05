from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /livre/5/node_detail/
    url(r'^(?P<node_id>[0-9]+)/node_detail/$', views.node_detail, name='node_detail'),
    # ex: /livre/5/node_detail/
    url(r'^(?P<edge_id>[0-9]+)/edge_detail/$', views.edge_detail, name='edge_detail'),

]
