from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView

from main.models import Request
from main.serializers import RequestCreateSerializer, RequestSerializer
from main.services import emulate_sending


class RequestAPIView(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer

    def perform_create(self, serializer):
        request = serializer.save()
        emulate_sending(request)


class HistoryAPIView(ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [SearchFilter]
    search_fields = ['cadastral_number']
