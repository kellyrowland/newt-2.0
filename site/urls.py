from django.urls import path
from site.views import *

urlpatterns = [
    path('datausage/<str:username>/', DataUsageView.as_view(), name='newt-site-data-usage'),
    path('userlargestfiles/<str:username>/', UserLargestFilesView.as_view(), name='newt-site-user-oldest-files'),
    path('useroldestfiles/<str:username>/', UserOldestFilesView.as_view(), name='newt-site-user-largest-files'),
    path('<str:query>/', ExtraAcctView.as_view()),
]
