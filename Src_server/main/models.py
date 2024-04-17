from django.db import models


class Event(models.Model):

    title = models.CharField('Название', max_length=50)
    data = models.DateTimeField('Дата и время начала', auto_now=False)
    place = models.CharField('Место проведения', max_length=250)
    place_link = models.CharField('Ссылка на место', max_length=250)
    guest = models.PositiveSmallIntegerField('Количество гостей')
    timeDuration = models.PositiveSmallIntegerField('Длительность мероприятия')
    dress_style = models.CharField('Дресс-код', max_length=40)
    price = models.IntegerField('Новая Цена')
    procents = models.IntegerField('Скидка Процентов')
    link_Album = models.CharField('Ссылка на альбом VK', max_length=250, default='#')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class EventLinks(models.Model):
    title = models.CharField('Подробнее', max_length=250, default='#')
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.event) + ' - ' + self.title

    class Meta:
        verbose_name = 'Описание События'
        verbose_name_plural = 'Описания Событий'


class lendingLinks(models.Model):
    title = models.CharField('Название', max_length=50, default='name')
    link1 = models.CharField('Ссылка баннер', max_length=250, default='#')
    link2 = models.CharField('Ссылка ноутбук', max_length=250, default='#')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылки на странице'
        verbose_name_plural = 'Ссылки на странице'


class Jobs(models.Model):
    title = models.CharField('Название', max_length=50, default='New')
    description = models.CharField('Описание вакансии', max_length=250)
    salary = models.IntegerField('Заработная плата')
    salaryDesc = models.CharField('Время заработка', max_length=25, default='смена')
    link = models.CharField('Ссылка на вакансию', max_length=250, default='https://t.me/chausmoscow_bot')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Docs(models.Model):
    title = models.CharField('Название', max_length=50, default='New')
    link = models.CharField('Ссылка на документ', max_length=250, default='#')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Partner(models.Model):
    title = models.CharField('Название', max_length=50, default='New')
    link = models.CharField('Ссылка на партнера', max_length=250, default='#')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class GuestList(models.Model):
    name = models.CharField('ФИО*', max_length=255)
    email = models.CharField('E-mail*', max_length=255)
    phone = models.CharField('Телефон*', max_length=20)
    promo = models.CharField('Промокод', max_length=20, null=True, blank=True)
    amount = models.IntegerField('Сумма', null=True)
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)
    status = models.CharField('Статус', max_length=30)
    order_id = models.CharField(blank=True, max_length=36, null=True, unique=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'