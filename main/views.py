import socket

from drf_spectacular.utils import extend_schema, OpenApiParameter, inline_serializer
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from main.models import Request
from main.serializers import RequestCreateSerializer, RequestSerializer
from main.services import emulate_sending


@extend_schema(
    summary="Создать запрос",
)
class RequestAPIView(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer

    def perform_create(self, serializer):
        request = serializer.save()
        emulate_sending(request=request)


@extend_schema(
    summary="Запросить результат",
    parameters=[
        OpenApiParameter(
            name='id',
            location=OpenApiParameter.PATH,
            description='id запроса',
            required=True,
            type=int)
    ],
)
class AnswerAPIView(RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


@extend_schema(
    summary="Посмотреть историю",
    parameters=[
        OpenApiParameter(
            name='search',
            location=OpenApiParameter.QUERY,
            description='Фильтр по кадастровому номеру',
            required=False,
            type=str)
    ],
)
class HistoryAPIView(ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [SearchFilter]
    search_fields = ['cadastral_number']


@extend_schema(
    summary="Проверить доступность сервера",
    responses={
        status.HTTP_200_OK: inline_serializer(
            name='PingResponse',
            fields={
                'message': serializers.CharField(),
            }
        )
    },
)
@api_view(http_method_names=['GET'])
def get_ping(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect(('0.0.0.0', '80'))
        s.shutdown(socket.SHUT_RDWR)
        return Response(status=status.HTTP_200_OK, data={"message": "server is available"})

    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "server is not available"})

    finally:
        s.close()
