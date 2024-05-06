from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug", blank=True, null=True)
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to="blog/photo", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_sign = models.BooleanField(default=True, verbose_name="Опубликовать")
    number_of_views = models.IntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
