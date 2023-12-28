from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название опроса')
    quantity_question = models.IntegerField(verbose_name='Количество вопросов')


    class Meta:
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'


    def __str__(self):
        return (
            f'{self.name}'
        )


class Question(models.Model):
    number = models.IntegerField(verbose_name='Номер вопроса')
    name = models.CharField(max_length=200, verbose_name='Название вопроса')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')


    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'


    def __str__(self):
        return (
            f'{self.number}.'
            f' {self.name}'
        )

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')


    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


    def __str__(self):
         return (
             f'{self.name}'
        )


class Answer(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')


    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'


    def __str__(self):
        return (
            f'Пользователь: {self.user.name}; '
            f'{self.name}'
        )
