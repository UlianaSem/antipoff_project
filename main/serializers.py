from rest_framework.serializers import ModelSerializer, SerializerMethodField

from main.models import Request, Answer


class RequestCreateSerializer(ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'


class RequestSerializer(ModelSerializer):
    answer = SerializerMethodField()

    class Meta:
        model = Request
        fields = '__all__'

    @staticmethod
    def get_answer(instance):
        try:
            result = Answer.objects.get(request=instance).value
        except Answer.DoesNotExist:
            result = None

        return result
