from django.db.models import Model, DecimalField, CharField, ForeignKey, BooleanField, CASCADE


"""Написать сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку 
запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. 
Считается, что внешний сервер может ответить true или false.
Данные запроса на сервер и ответ с внешнего сервера должны быть сохранены в БД. Нужно написать АПИ для получения
 истории всех запросов/истории по кадастровому номеру."""

class Request(Model):
    cadastral_number = CharField(max_length=15, verbose_name='кадастровый номер')
    latitude = DecimalField(max_digits=6, decimal_places=2, verbose_name='широта')
    longitude = DecimalField(max_digits=6, decimal_places=2, verbose_name='долгота')

    def __str__(self):
        return self.cadastral_number

    class Meta:
        verbose_name = 'запрос'
        verbose_name_plural = 'запросы'


class Answer(Model):
    request = ForeignKey(Request, on_delete=CASCADE, related_name='answer', verbose_name='запрос')
    value = BooleanField(verbose_name='значение ответа')

    def __str__(self):
        return f'{self.request} - {self.value}'

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
