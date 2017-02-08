from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^voa/$',
        views.VOACreateView.as_view(), name='voa-create'),
]
