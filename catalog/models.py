from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название товара",
        help_text="Введите название товара"
    )
    description = models.TextField(
        max_length=150,
        verbose_name="Описание товара",
        help_text="Введите описание товара",
    )
    preview = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Фото (превью)",
        help_text="Загрузите фото товара",
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите название категории",
        null=True,
        blank=True,
        related_name='products'
    )
    price = models.IntegerField(
        verbose_name="Цена товара", help_text="Введите цену товара"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", help_text="Введите дату создания"
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения", help_text="Введите дату изменения"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        max_length=150,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
