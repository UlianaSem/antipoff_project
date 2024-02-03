from django.urls import path

from main.apps import MainConfig
from main.views import RequestAPIView, HistoryAPIView

app_name = MainConfig.name


urlpatterns = [
    path('query/', RequestAPIView.as_view(), name='request_fulfillment'),
    # path('result/', ..., name='result_receipt'),
    # path('ping/', ..., name='check'),
    path('history/', HistoryAPIView.as_view(), name='history_receipt'),
]
