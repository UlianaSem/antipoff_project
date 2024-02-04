import threading

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from main.models import Request
from main.serializers import RequestCreateSerializer, RequestSerializer
from main.services import emulate_sending


class RequestAPIView(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer

    def perform_create(self, serializer):
        request = serializer.save()
        thread = threading.Thread(target=emulate_sending, args=[request], name='emulate')
        thread.start()


class AnswerAPIView(RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class HistoryAPIView(ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [SearchFilter]
    search_fields = ['cadastral_number']


@api_view(http_method_names=['GET'])
def get_ping(request):
    threads = [thread.name for thread in threading.enumerate()]

    if 'emulate' in threads:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "server is not available"})

    return Response(status=status.HTTP_200_OK, data={"message": "server is available"})
