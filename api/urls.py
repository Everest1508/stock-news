from django.urls import path
from .views import GetContentAPIView,GetSubjectAPIView,FileAPIView

urlpatterns = [
    path('get-subject/',GetSubjectAPIView.as_view(),name="get-subject"),
    path('get-content/',GetContentAPIView.as_view(),name="get-content"),
    path('download-file/',FileAPIView.as_view(),name="get-file"),
]
