from django.conf.urls import url
from .views import PublicacionListView,PublicacionCreateView

urlpatterns = [
    url(r'^$', PublicacionListView.as_view(), name="list"),
    url(r'^new/$', PublicacionCreateView.as_view(),name="new"),
]
