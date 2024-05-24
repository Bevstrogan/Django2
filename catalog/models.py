from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    image_preview = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Фото(превью)",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    publication_sign = models.BooleanField(verbose_name='Признак публикации', default=False, help_text="Укажите признак публикации")

    owner = models.ForeignKey(User, verbose_name='Имя создателя', help_text='Укажите имя создателя товара', blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]
        permissions = [
            ("can_edit_publication_sign", "Can edit publication sign"),
            ("can_edit_description", "Can edit description"),
            ("cand_change_category", "Cand change category")
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Version(models.Model):
    name = models.ForeignKey(
        Product,
        verbose_name="продукт",
        on_delete=models.CASCADE,
        related_name="versions",
    )
    version_number = models.PositiveIntegerField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    version_now = models.BooleanField(
        default=True, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return f"{self.version_name} | {self.version_number}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
