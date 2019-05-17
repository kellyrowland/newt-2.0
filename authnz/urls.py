from django.urls import path
from authnz.views import AuthView, ExtraAuthView

urlpatterns = [
    path('', AuthView.as_view()),
    path('<str:query>', ExtraAuthView.as_view()),
]
    
