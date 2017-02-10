from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^voa/$',
        views.VOACreateView.as_view(), name='voa-create'),
    url(
        r'^voa/(?P<uarn>[a-zA-Z0-9]+)/$',
        views.VOADetailView.as_view(), name='voa-detail'),
]
