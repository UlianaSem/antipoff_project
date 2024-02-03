import random
import time

from main.models import Answer, Request


def emulate_sending(request):
    time.sleep(random.randint(0, 60))
    result = random.choice([True, False])

    Answer.objects.create(request=request, value=result)
