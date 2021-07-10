from django.db import models
class achievements(models.Model):
    achievement_name = models.CharField('Ачивка', max_length=100)
    class Meta:
        verbose_name = "Ачивка"
        verbose_name_plural = "Ачивки"

    def __str__(self):
        return self.achievement_name
class lists(models.Model):
    list_name = models.CharField('Группа заданий', max_length=100)
    class Meta:
        verbose_name = "Группа заданий"
        verbose_name_plural = "Группы заданий"

    def __str__(self):
        return self.list_name

class events(models.Model):
    event_name = models.CharField('Событие', max_length=100)
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.event_name

class prioriry(models.Model):
    prioriry_name = models.CharField('Приоритет', max_length=100)
    class Meta:
        verbose_name = "Приоритет"
        verbose_name_plural = "Типы приоритетов"

    def __str__(self):
        return self.prioriry_name

class families(models.Model):
    family_name = models.CharField('Названия семьи', max_length=100)
    class Meta:
        verbose_name = "Названия семьи"
        verbose_name_plural = "Названия семей"

    def __str__(self):
        return self.family_name
class comments(models.Model):
    comment = models.TextField('Комментарий')
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.comment


class users(models.Model):
    username = models.CharField('Имя пользователя', max_length=50)
    amout_task = models.IntegerField('Количество активных задач')
    amout_task_end = models.IntegerField('Количество выполненных задач')
    family_id = models.ForeignKey(
        families,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Семья'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
class score(models.Model):
    # user_id = models.IntegerField('Код пользователя')
    score = models.IntegerField('Колисчество выполненных задач')
    user_id = models.ForeignKey(
        users,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь'
    )
    class Meta:
        verbose_name = "Рекорд"
        verbose_name_plural = "Рекорды"

    def __str__(self):
        return str(self.score)

class score_points(models.Model):
    # user_id = models.IntegerField('Код пользователя')
    score = models.IntegerField('Набранные баллы')
    user_id = models.ForeignKey(
        users,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь'
    )
    class Meta:
        verbose_name = "Набранные баллы"
        verbose_name_plural = "Набранные баллы"

    def __str__(self):
        return str(self.score)


class task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    task_date = models.DateField('Дата задания')
    status = models.BooleanField('Статус задачи')
    points = models.IntegerField('Количество очков', default=100)

    user_id = models.ForeignKey(
        users,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Пользовательывыв'
    )
    comment_id = models.ForeignKey(
        comments,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Коментарий'
    )
    prioriry_id = models.ForeignKey(
        prioriry,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Тип приоритета'
    )
    achievement_id = models.ForeignKey(
        achievements,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Достижение'
    )
    list_id = models.ForeignKey(
        lists,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Участвует в списке'
    )
    event_id = models.ForeignKey(
        events,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Участвует в событии'
    )

    

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title

    