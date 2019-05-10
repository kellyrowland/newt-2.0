from django.conf.urls import url
from authnz.views import AuthView, ExtraAuthView


urlpatterns = [
    url(r'^$', AuthView.as_view()),
    url(r'^(?P<query>.+)/$', ExtraAuthView.as_view()),
]
    
