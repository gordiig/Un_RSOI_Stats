from django.conf.urls import url
from RequestStats import views


urlpatterns = [
    url(r'^requests/$', views.RequestsStatsListView.as_view()),
    url(r'^requests/(?P<pk>\d+)/$', views.RequestsStatsDetailView.as_view()),
]
