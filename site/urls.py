from django.urls import path
from site.views import *

urlpatterns = [
    path('datausage/', DataUsageView.as_view(), name='newt-site-data-usage'),
    path('userlargestfiles/', UserLargestFilesView.as_view(), name='newt-site-user-oldest-files'),
    path('useroldestfiles/', UserOldestFilesView.as_view(), name='newt-site-user-largest-files'),
    path('<str:query>/', ExtraAcctView.as_view()),
]
