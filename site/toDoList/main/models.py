from django.db import models

class users(models.Model):
    username = models.CharField('Имя пользователя', max_length=50)
    amout_task = models.IntegerField('Количество активных задач')
    amout_task_end = models.IntegerField('Количество выполненных задач')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

class task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    task_date = models.DateField('Дата задания')
    status = models.BooleanField('Статус задачи')
    points = models.IntegerField('Количество очков', default=100)
    # user_id = models.IntegerField('Код пользователя')
    user_id = models.ForeignKey(
        users,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title


class score(models.Model):
    # user_id = models.IntegerField('Код пользователя')
    score = models.IntegerField('Колисчество выполненных задач')
    
    
    user_id = models.ForeignKey(
        users,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь'
    )
    # score = models.ForeignKey(
    #     users(amout_task_end),
    #     on_delete=models.CASCADE,
    #     null=True,
    #     verbose_name='Рекорд'
    # )

    class Meta:
        verbose_name = "Рекорд"
        verbose_name_plural = "Рекорды"

    def __str__(self):
        return str(self.score)

    