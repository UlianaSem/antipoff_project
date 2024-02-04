from django.urls import path

from main.apps import MainConfig
from main.views import RequestAPIView, HistoryAPIView, AnswerAPIView, get_ping

app_name = MainConfig.name


urlpatterns = [
    path('query/', RequestAPIView.as_view(), name='request_fulfillment'),
    path('result/<int:pk>/', AnswerAPIView.as_view(), name='result_receipt'),
    path('ping/', get_ping, name='check'),
    path('history/', HistoryAPIView.as_view(), name='history_receipt'),
]
